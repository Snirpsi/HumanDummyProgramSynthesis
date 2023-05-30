#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and iterates over all ports. """    
    
    from wsgiref.simple_server import make_server
    
    httpd = make_server('localhost', 8080, app)
    httpd.serve_forever()
    
