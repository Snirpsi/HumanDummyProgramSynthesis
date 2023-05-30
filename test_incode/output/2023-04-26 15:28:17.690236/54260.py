#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or converts a port. """    
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(0)
    
    web