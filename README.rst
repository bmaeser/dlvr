=====
dlvr
=====

Email sending for humans

Installation
------------

with pip as easy as: ::

    $ pip install dlvr

or checkout the latest version from github: ::

    $ git clone https://github.com/bmaeser/dlvr.git
    $ cd dlvr
    $ python setup.py install

Usage
------------------

open a connection to a server: ::

	>>> from dlvr import SMTPServer
	>>> s = SMTPServer()

create a email: ::

	>>> from dlvr import Message
	>>> m = Message('bob@example.com', ['alice@gmail.com', 'support@example.com'],
			'testsubject', 'testbody')

send the email: ::

	>>> s.connect()
	>>> s.send(m)
	>>> s.disconnect()