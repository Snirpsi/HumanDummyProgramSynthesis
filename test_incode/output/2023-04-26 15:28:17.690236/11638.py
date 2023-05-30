#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or iterates over numbers. """    
    import sys
    import cgi
    import random
    
    form = cgi.FieldStorage()
    
    number = int(form.getvalue