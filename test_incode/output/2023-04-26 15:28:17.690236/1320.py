#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    from flask import Flask, request
    app = Flask(__name__)
    app.run(host='0.0.0.0', port=8080, debug=True)
<|/ file ext=.py source=github |>