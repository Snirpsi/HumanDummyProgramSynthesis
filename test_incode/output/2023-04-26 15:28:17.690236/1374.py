#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    from flask import Flask
    app = Flask(__name__)
    app.run(host='0.0.0.0')

<|/ file source=github ext=.py filename=server.py |>