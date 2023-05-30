#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    from flask import Flask
    app = Flask(__name__).route('/fruits')
    def fruits():
        """ Return a list of fruits. """
        fruits = ['apple', 'orange', 'banana', 'cherry']
        return 