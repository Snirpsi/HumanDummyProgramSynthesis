#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports and calculates user input. """    
    ports = [80, 443]
    
    server_address = ("", ports[0])
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
