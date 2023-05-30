#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    
    from flask import Flask, request, jsonify, abort
    
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        """ Return all ports """
        return jsonify({'ports': [i.port for i in 