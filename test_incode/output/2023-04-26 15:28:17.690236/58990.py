#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or converts words. """    
    port = int(sys.argv[1])
    webserver.serve_forever(port)
