#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers or opens a port. """    
    port = int(sys.argv[1])
    
    webserver.run(port)
    
