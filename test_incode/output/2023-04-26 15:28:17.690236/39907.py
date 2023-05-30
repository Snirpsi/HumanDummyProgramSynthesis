#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports.sort()
    
    server = HTTPServer(('', ports[0]), Handler)
    server.serve_forever()
    
