#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words or prints a list of words. """    
    
    # Create the webserver
    webserver = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start the webserver
    webserver.serve_forever()
    
