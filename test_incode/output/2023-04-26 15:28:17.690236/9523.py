#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    from flask import Flask, render_template, request
    app = Flask(__name__) 
    app.run(host='0.0.0.0', port=5000)
