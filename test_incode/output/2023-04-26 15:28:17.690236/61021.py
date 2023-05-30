#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports and converts words. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    server = HTTPServer(('', ports[0]), SimpleHTTPRequestHandler)
    
    for port in ports[1:]:
        server.