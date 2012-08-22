# -*- encoding: utf-8 -*-

import os
import mimetypes

from email import encoders
from email.utils import formataddr
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Message(object):

    def __init__(self, from_email, to, subject, text_message=None, cc=None,
        bcc=None, attachments=None, alternatives=None, charset=None):
        """
        Constructor for a Email Message

        Required Parameters:

        :param from_email: the senders emailadress

        :param to: the recipients of this email, a list of strings

        :param subject: the subject of this email



        """
        self.from_email = from_email
        self.to = to
        self.subject = subject

        self.text_message = text_message or ''
        self.charset = charset or 'utf-8'
        self.cc = cc or []
        self.bcc = bcc or []
        self.alternatives = alternatives or []
        self.attachments = attachments or []


    def recipients(self):
        """
        Returns all recipients of this Message.
        includes: to, cc and bcc
        """
        return self.to + self.cc + self.bcc

    def message(self):
        """
        Returns a email.message.Message / MIME version of this Message.
        """

        ## we have no attachments or alternative content --> simple text mail
        if not self.alternatives and not self.attachments:
            msg = MIMEText(self.text_message, 'plain', self.charset)
        ## we need a multipart/mixed container
        elif self.alternatives:
            msg = MIMEMultipart('mixed')
            container = MIMEMultipart('alternative')

            txtmsg = MIMEText(self.text_message, 'plain', self.charset)
            container.attach(txtmsg)
            for content, mtype in self.alternatives:
                maintype, subtype = mtype.split('/', 1)
                alternatemsg = MIMEText(content, subtype)
                container.attach(alternatemsg)
            msg.attach(container)
        else:
            msg = MIMEMultipart('mixed')
            txtmsg = MIMEText(self.text_message, 'plain', self.charset)
            msg.attach(txtmsg)

        if self.attachments:
            for path, mtype in self.attachments:
                if not mtype: ## try to guess
                    t, enc = mimetypes.guess_type(path)
                    mtype = t
                if not mtype: ## default mimetype
                    mtype = 'application/octet-stream'

                content = open(path, 'rb').read()
                maintype, subtype = mtype.split('/', 1)
                filename = os.path.basename(path)

                if maintype == 'text':
                    inner = MIMEText(content, _subtype=subtype)
                elif maintype == 'image':
                    inner = MIMEImage(content, _subtype=subtype)
                elif maintype == 'audio':
                    inner = MIMEAudio(content, _subtype=subtype)
                else:
                    inner = MIMEBase(maintype, subtype)
                    inner.set_payload(content)
                    encoders.encode_base64(inner)
                inner.add_header('Content-Disposition', 'attachment',
                    filename=filename)
                msg.attach(inner)

        ## message headers
        msg['From'] = self.from_email
        msg['To'] = ', '.join(str(i) for i in self.to)
        msg['Subject'] = self.subject
        if self.cc:
            msg['Cc'] = ', '.join(str(i) for i in self.cc)
        if self.bcc:
            msg['Bcc'] = ', '.join(str(i) for i in self.bcc)

        return msg

    def attach_alternative(self, content, mimetype='text/html'):
        """
        attach an alternative content representation

        :param content: content to attach
        :param mimetype: the mimetype of given content, defaults to 'text/html'
        """
        self.alternatives.append((content, mimetype))

    def attach_file(self, filepath, mimetype=None):
        """
        attach a file from the filesystem as a attachment

        :param filepath: (required) the location of your file on your filesystem
        :param mimetype: (optional) the mimetype of given attachment
            if no mimetype is given the type will be guessed from the filename
        """
        self.attachments.append((filepath, mimetype))

