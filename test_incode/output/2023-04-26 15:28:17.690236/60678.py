#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    from flask import Flask
    app = Flask(__name__) # create a flask application
    app.debug = True # enable flask debugging
    app.secret_key = 'super secret key' # set secret key
    app.run(host='0.0.0.0', port=5000, debug=True) # run server
