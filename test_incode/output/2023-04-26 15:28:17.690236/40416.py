#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    
    # Create a simple webserver
    webserver = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Listen for connections
    webserver.serve_forever()
    
