#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or prints a list of numbers. """    
    
    import os
    import sys
    
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    from webserver import WebServer
    
    server = WebServer()
    server.serve_forever()
    
