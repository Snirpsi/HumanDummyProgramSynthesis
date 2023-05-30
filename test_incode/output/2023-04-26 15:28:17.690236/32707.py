#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    import os
    
    port = int(sys.argv[1])
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from webserver import webserver
    
    webserver.serve_forever(port=port)

<|/ file ext=.py filename=webserver.py |>