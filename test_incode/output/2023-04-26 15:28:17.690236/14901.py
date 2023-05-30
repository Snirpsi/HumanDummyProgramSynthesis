#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    import sys
    
    web = WebServer()
    web.serve_forever()
    
