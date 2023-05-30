#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or adds words. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Starting httpd...