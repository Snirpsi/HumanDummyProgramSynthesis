#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or prints numbers. """    
    port = int(sys.argv[1])
    
    # Remove port if port is given
    if port > 0:
        