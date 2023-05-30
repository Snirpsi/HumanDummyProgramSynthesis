#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports or returns user input. """    
    ports = input("Enter ports to listen on: ")
    ports = ports.split()
    ports = [int(port) for port in ports]
    ports.sort()
    
    server = HTTPServer(('', ports[0]), SimpleHTTPRequestHandler)
    
    server.serve_forever()
