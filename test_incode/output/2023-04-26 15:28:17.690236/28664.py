#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or opens words. """    
    import sys
    port = int(sys.argv[1])
    
    webserver.run(port)
