# -*- encoding: utf-8 -*-

import smtplib


class SMTPServer(object):

    def __init__(self, host="localhost", port="25", auth_user=None,
        auth_pass=None,	tls=False):

        self.host = host
        self.port = port
        self.auth_user = auth_user
        self.auth_pass = auth_pass
        self.tls = tls

        self._connection = None

    def connect(self):
        """
        Opens a connection to the SMTP-Server
        """
        self._connection = smtplib.SMTP(self.host, self.port)
        #be nice and say hello
        self._connection.ehlo()

        ## encrypt this session
        if self.tls and self._connection.has_extn('STARTTLS'):
            self._connection.starttls()
            self._connection.ehlo()

        ## authenticate
        if self.auth_user is not None:
            self._connection.login(self.auth_user, self.auth_pass)

    def disconnect(self):
        """
        Closes the connection to the SMTP-Server
        """
        if self._connection is not None:
            self._connection.quit()
            self._connection = None

    def send(self, message):
        """
        Sends a message to the SMTPServer.
        :param message: a instance of dlvr.Message
        """
        self._connection.sendmail(message.from_email, message.recipients(),
            message.message().as_string())
        pass

    def send_email(self, message):
        """
        shorthand for:
        >>> connect()
        >>> send(message)
        >>> disconnect()
        Use this if you want to send only one message, otherwise reuse the open
        connection and close it manually.
        """
        self.connect()
        self.send(message)
        self.disconnect()
