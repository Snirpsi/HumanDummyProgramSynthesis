#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and opens a port. """    
    
    ports = range(8000, 9000)
    
    server_address = ("", 9000)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
