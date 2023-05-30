#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    
    port = 8080
    
    # Create a simple HTTP server
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    
    # Start the server
    httpd.serve_forever()
    
