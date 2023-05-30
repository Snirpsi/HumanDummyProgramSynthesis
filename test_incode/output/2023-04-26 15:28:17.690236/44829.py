#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input or enumerates numbers. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
