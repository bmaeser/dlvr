#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class Message(object):

    def __init__(self, from_email, recipient_list=[], subject="", message=""):
        self.from_email = from_email
        self.recipient_list = recipient_list
        self.subject = subject
        self.message = message
