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

Quickstart
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



Full example ::
------------------

	from dlvr import SMTPServer, Message

	server = SMTPServer(host="smtp.googlemail.com", port='587',
		auth_user='MYUSERNAME',	auth_pass='MYPASSWOR', tls=True)

	## host (optional): defaults to localhost
	## port (optional): defaults to 25
	## auth_user (optional): your usernamer
	## auth_pass (optional): your passwort
	## tls (optional): encrypt the session defaults to False 