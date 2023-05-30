#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    from flask import Flask
    app = Flask(__name__).route('/')
    app.