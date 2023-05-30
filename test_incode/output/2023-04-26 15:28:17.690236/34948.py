#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    webserver = Webserver()
    webserver.serve_forever()
    
