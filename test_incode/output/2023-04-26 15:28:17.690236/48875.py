#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and iterates over user input. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
