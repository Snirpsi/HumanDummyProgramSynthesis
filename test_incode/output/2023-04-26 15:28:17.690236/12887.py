#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    import sys
    
    web = WebServer()
    web.serve_forever()
    
