#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    
    from wsgiref.simple_server import make_server
    
    httpd = make_server('localhost', 8080, MyApp)
    
    httpd.serve_forever()

<|/ file source=github filename=webserver.py |>