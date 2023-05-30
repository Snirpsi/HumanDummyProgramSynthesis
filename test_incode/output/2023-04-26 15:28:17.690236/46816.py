#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    from flask import Flask
    app = Flask(__name__, static_url_path='')
    app.run(host='0.0.0.0', port=8080, debug=True)

<|/ file filename=fruits.py ext=.py |>