#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and prints fruits. """    
    
    import os
    import sys
    
    port = int(sys.argv[1])
    
    webserver = WebServer()
    webserver.serve_forever()
    
