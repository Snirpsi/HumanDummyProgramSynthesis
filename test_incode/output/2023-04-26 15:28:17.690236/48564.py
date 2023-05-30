#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or returns fruits. """    
    from flask import Flask
    app = Flask(__name__)
    app.run(host='0.0.0.0', port=8080)
