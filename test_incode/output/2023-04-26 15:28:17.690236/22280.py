#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers. """    
    
    # Create a simple webserver
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()

<|/ file ext=.py |>