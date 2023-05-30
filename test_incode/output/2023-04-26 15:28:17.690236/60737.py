#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers and iterates over words. """    
    
    # Create a webserver
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()
