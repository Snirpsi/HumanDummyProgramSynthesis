#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports. """    
    ports = [int(port) for port in range(8000, 9001)]
    
    server_address = ("", 8000)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    for port in ports:
        httpd.