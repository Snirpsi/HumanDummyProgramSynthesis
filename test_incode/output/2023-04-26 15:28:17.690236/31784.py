#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and converts a port. """    
    port = int(sys.argv[1])
    
    webserver.serve_forever(port)
    
