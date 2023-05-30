#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or calculates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    webserver = WebServer()
    webserver.serve_forever()
    
