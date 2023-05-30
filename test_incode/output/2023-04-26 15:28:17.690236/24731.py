#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    from flask import Flask, render_template, request
    app = Flask(__name__, static_url_path='')
    app.debug = True
    app.secret_key = 'super secret key'
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/fruits', 'fruits', fruits)
    app.add_url_rule('/fruits/<string:fruit>', 'fruit', fruit)
    app.add_url_rule('/fruits/<string:fruit>/