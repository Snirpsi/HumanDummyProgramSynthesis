#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    from flask import Flask, render_template, request, jsonify
    app = Flask(__name__, static_url_path='/static')
    app.