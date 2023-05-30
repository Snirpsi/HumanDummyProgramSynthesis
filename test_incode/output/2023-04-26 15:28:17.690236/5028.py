#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    import sys
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, MyHandler)
    httpd.serve_forever()
</code>
<|/ a |>
<| c |>
This works great. Thanks!
<|/ c |>
<| a tags=python,python-3.x,webserver,flask |>
I used the code below to run flask app on my local machine. Hope it helps.
<code>
from flask import Flask
app = Flask(__name__).route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't answer the question. OP wants to run a web server on his local machine.
<|/ c |>
<| c |>
This code runs flask app on my local machine.
<|/ c |>
<| c |>
I used the code below to run flask app on my local machine. Hope it helps.
<|/ c |>
<| a dscore=0 tags=python,python-3.x,webserver,flask |>
<code>
from flask import Flask
app = Flask(__name__).route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
</code>
<|/ a |>