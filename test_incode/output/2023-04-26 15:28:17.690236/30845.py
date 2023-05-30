#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    from wsgiref.simple_server import make_server
    
    server = make_server('localhost', 8000, FruitEnumerator)
    server.serve_forever()
    
