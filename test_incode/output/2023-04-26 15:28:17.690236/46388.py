#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits or returns fruits. """    
    from flask import Flask
    from flask import request
    app = Flask(__name__) # create our flask app
    app.debug = True # enable debugging
    app.run(host='0.0.0.0', port=8080) # run the app
    
<|/ file source=github ext=.py |>