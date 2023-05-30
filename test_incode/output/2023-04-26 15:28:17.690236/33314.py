#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or prints words. """    
    import sys
    port = int(sys.argv[1])
    webserver.run(port)
