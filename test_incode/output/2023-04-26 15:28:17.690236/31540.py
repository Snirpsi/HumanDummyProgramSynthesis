#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers. """    
    
    port = 8080
    
    # Create a simple webserver
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()
