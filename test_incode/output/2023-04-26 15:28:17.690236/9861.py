#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and opens a list of numbers. """    
    import sys
    import socketserver
    import cgi
    import random
    from 