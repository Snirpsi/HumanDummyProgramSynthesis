#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/fruits')
    def fruits():
        """ Return all fruits. """
        fruits = ['apple', 'banana', 'cherry']
        return 