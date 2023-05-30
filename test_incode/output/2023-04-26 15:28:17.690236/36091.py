#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    ports = []
    
    for port in range(1, 65535):
        ports.append(port)
    
    server = HTTPServer(('', 0), SimpleHTTPRequestHandler)
    
    for port in ports:
        server.