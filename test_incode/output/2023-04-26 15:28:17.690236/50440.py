#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and adds a port. """    
    port = int(sys.argv[1])
    webserver.run(port=port)
    
