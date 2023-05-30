#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    from flask import Flask
    app = Flask(__name__) # create the flask app
    app.debug = True # enable debugging
    app.run(host='0.0.0.0', port=5000, debug=True) # run the flask app
