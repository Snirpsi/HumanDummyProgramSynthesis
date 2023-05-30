#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    import sys
    from wsgiref.simple_server import make_server
    
    httpd = make_server('', 8000, app)
    httpd.serve_forever()

<|/ file source=github ext=.py |>