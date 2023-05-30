#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or iterates over user input. """    
    
    # Create the webserver
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Run the webserver
    server.serve_forever()
    
