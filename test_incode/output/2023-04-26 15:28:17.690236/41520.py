#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    
    import sys
    
    port = sys.argv[1]
    
    web = WebServer(port)
    web.serve()
    
    
