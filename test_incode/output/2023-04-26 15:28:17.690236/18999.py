#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port. """    
    port = sys.argv[1]
    webserver.serve(port)
