#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    import sys
    import os
    import http.server
    import socketserver
    import random
    import webbrowser
    from 