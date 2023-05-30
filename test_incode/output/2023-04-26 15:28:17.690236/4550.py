#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    from flask import Flask
    app = Flask(__name__).route('/fruits')
    def fruits():
        """ Enumerates fruits. """
        return ['apple', 'banana', 'cherry']
    app.run(host='0.0.0.0', port=5000)
