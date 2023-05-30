#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    from flask import Flask
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', port=5000)
