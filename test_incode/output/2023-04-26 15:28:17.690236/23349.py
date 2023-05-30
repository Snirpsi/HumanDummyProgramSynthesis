#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    # Create a simple web server
    httpd = HTTPServer(("", 80), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()
