#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    from flask import Flask
    app = Flask(__name__)
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
<|/ file ext=.py source=github |>