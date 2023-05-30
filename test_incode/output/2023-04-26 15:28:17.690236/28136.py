#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or adds all ports. """    
    port = int(sys.argv[1])
    
    if port > 0:
        webserver.run(port=port)
    else:
        webserver.run(port=webserver.port)
    
