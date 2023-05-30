#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    from flask import Flask
    from flask import request
    from flask import render_template
    from flask import send_from_directory
    from flask import Response
    from flask import url_for
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'super secret key'
    app.add_url_rule('/fruits/<string:fruit>', 'fruit', 