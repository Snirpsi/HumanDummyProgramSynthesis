#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports.sort()
    
    web = WebServer(ports)
    web.serve_forever()
