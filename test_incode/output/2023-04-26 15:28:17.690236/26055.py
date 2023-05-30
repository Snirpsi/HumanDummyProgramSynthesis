#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or calculates fruits. """    
    
    import sys
    
    webserver = WebServer()
    webserver.serve_forever()
    
    
