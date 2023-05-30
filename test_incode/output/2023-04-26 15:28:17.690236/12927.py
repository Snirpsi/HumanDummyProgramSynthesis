#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import math

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Get a number from query string. """
            number = self.path.split('?')[0]
            number = int(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert string to number. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
            number = str(number)
            
            """ Convert number to string. """
            number = float(number)
            
            """ Convert number to string. """
