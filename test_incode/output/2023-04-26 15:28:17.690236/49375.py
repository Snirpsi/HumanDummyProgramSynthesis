#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input. """    
    from flask import Flask
    app = Flask(__name__, static_url_path='')
    app.