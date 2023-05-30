#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    from wsgiref.simple_server import make_server
    import sys
    httpd = make_server('localhost', 8080, FruitHandler)
    httpd.serve_forever()

<|/ file ext=.py |>