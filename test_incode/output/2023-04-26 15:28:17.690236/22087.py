#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or opens numbers. """    
    from wsgiref.simple_server import make_server
    
    httpd = make_server('', 8000, MyHandler)
    httpd.serve_forever()

<|/ file filename=server.py source=github |>