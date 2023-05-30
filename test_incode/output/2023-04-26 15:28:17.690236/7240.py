#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words or multiplyes a list of numbers. """    
    
    import sys
    
    server_address = ('localhost', 8000)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Starting httpd on port 8000...')
    httpd.serve_forever()
    
