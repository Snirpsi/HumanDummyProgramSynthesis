#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or adds fruits. """    
    from wsgiref.simple_server import make_server
    import sys
    
    port = sys.argv[1]
    
    httpd = make_server('localhost', port, FruitHandler)
    httpd.serve_forever()
    
