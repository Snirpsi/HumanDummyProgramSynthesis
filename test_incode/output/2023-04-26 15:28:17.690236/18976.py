#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    from wsgiref.simple_server import make_server
    
    httpd = make_server('localhost', 8000, FruitApp)
    httpd.serve_forever()
    
