# -*- encoding: utf-8 -*-

from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Message(object):

    def __init__(self, from_email, to, subject, text_message='', cc=[], bcc=[]):
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
        self.text_message = text_message
        self.cc = cc
        self.bcc = bcc


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

        msg = MIMEText(self.text_message)
        msg['From'] = self.from_email
        msg['To'] = ', '.join(str(i) for i in self.to)
        msg['Subject'] = self.subject

        return msg





## todo:
# not ugly from/to/cc/bcc addresses: 'my name <me@asdf.com>'
# 