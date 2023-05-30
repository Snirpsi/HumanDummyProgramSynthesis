#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    from flask import Flask
    app = Flask(__name__).route('/')
    app.add_url_rule('/fruits/<string:fruit>', 'fruit', 