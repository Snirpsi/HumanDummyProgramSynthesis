#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    server = HTTPServer(('', 0), MyHandler)
    
    for port in ports:
        server.