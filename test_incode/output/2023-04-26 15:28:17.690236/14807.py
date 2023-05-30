#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or enumerates a list of numbers. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    
    from webserver import webserver
    
    webserver.serve_forever()
    
