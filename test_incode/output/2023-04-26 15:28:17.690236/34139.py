#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits or adds numbers. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from webserver import WebServer
    
    server = WebServer()
    server.serve()
    
