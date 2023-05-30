#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers. """    
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from webserver import webserver
    webserver.main()

<|/ file ext=.py |>