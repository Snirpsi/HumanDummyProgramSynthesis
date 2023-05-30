#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and opens numbers. """    
    
    # Open the port and wait for connections
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
