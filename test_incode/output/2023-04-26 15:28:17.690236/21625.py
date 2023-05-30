#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or enumerates numbers. """    
    
    # Define the webserver
    webserver = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Open the webserver
    webserver.serve_forever()
    
