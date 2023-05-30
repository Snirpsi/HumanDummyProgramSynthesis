#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from wsgiref.simple_server import make_server
    
    server_address = (sys.argv[1], int(sys.argv[2]))
    
    httpd = make_server(*server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
