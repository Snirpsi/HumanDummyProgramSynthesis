#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    from wsgiref.simple_server import make_server
    
    httpd = make_server('localhost', 8000, FruitEnumerator)
    httpd.serve_forever()
    
