#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input and prints a list of numbers. """    
    
    # Create a simple webserver
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Listen for connections
    httpd.serve_forever()
