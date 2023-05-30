#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    from wsgiref.simple_server import make_server
    
    httpd = make_server('localhost', 8080, FruitHandler)
    httpd.serve_forever()
