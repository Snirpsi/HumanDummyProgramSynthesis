#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and returns fruits. """    
    from flask import Flask
    from flask import request
    from flask import jsonify
    from flask import render_template
    from flask import Response
    from flask import url_for
    app = Flask(__name__, static_url_path='')
    app.debug = True
    app.secret_key = 'super secret key'
    app.register_blueprint(