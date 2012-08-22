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



Full example 
------------------

::

    from dlvr import SMTPServer, Message

    server = SMTPServer(host="smtp.googlemail.com", port='587',
        auth_user='MYUSERNAME', auth_pass='MYPASSWOR', tls=True)

    ## host (optional): defaults to localhost
    ## port (optional): defaults to 25
    ## auth_user (optional): your usernamer
    ## auth_pass (optional): your passwort
    ## tls (optional): encrypt the session defaults to False

    text = 'here is you link: http://www.google.com'
    subject = 'the link you asked for'

    html = """\
    <html>
        <head></head>
        <body>
            <p>Hi!<br>
            Here is the <a href="http://www.google.com">link to google</a> you wanted.
            </p>
        </body>
    </html>
    """

    message = Message('bob@example.com', ['alice@gmail.com', 'support@example.com'],
        subject, text, alternatives=[(html, 'text/html')])

    ## constructor arguments:

    ## from_email: required, the senders email
    ## to: required, a list of recipients
    ## subject: required, the emails subject
    ## text_message (optional): the text representation of the email body
    ## cc (optional): a list of the carbon-copy recipients
    ## bcc (optional): a list of blind-carbon-copy recipients
    ## attachments (optional): a list of attachments, and the mimetype to use eg:
    ##      attachments = [('/tmp/image.jpg', 'image/jpeg'), ('/tmp/song.mp3', 'audio/mpeg3')]
    ## alternatives (optional): a list of alternative representation of the email body
    ##      and the mimetype to use
    ## charset (optional): the charset/encoding to use for text_message, defaults to utf-8

    ## message functions:

    # attach_alternative(content, 'mimetype')
    # where mimetype is optional und defaults to 'text/html'

    # attach_file('/path/to/file', 'mimetype')
    # where mimetype is opional and is guessed if not provided

    server.connect()
    server.send(message)
    ## send another message with the same open connection ...
    server.disconnect()

    ## or shorthand if you only send one message:
    server.send_email(message)

Contribute
------------------

pull-request please and/or create a issue on github
