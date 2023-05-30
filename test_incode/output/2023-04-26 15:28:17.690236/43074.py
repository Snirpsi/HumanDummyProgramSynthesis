#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or enumerates fruits. """    
    
    port = int(sys.argv[1])
    
    # Remove a port if requested.
    if port != 80:
        server.