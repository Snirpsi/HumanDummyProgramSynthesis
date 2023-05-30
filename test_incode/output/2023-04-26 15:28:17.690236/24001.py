#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    import sys
    
    web = WebServer()
    web.serve()
    
    sys.exit()
    
