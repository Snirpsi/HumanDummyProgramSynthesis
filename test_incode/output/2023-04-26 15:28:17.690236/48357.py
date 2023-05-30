#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or iterates over all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8080
    
    webserver.serve(port, webserver.app)
    
