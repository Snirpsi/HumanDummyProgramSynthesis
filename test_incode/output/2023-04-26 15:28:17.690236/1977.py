#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers and stores a list of words. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
