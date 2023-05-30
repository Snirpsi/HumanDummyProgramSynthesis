#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or multiplyes user input. """    
    
    # Create the webserver
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Start the webserver
    server.serve_forever()
    
