#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    from flask import Flask, render_template, request
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'secret'
    fruits = 