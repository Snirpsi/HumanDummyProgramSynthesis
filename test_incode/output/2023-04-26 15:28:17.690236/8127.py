#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and stores a port. """    
    port = int(sys.argv[1])
    
    webserver.serve(port, webserver.app)
    
