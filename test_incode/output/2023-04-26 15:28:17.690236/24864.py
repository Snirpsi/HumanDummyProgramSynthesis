#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or multiplyes fruits. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from webserver import webserver
    
    webserver.run(host='0.0.0.0', port=8080)
