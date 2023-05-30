#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    # Create a simple webserver
    httpd = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()
