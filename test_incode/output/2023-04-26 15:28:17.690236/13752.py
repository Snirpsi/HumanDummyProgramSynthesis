#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or adds a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '80'
    
    webserver.serve(port)
    
