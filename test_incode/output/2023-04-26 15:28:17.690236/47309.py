#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or opens all ports. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
