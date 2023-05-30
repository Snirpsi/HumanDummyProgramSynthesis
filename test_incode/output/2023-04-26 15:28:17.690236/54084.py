#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or adds a list of words. """    
    
    import sys
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
