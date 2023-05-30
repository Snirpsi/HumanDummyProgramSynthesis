#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    # Create a simple web server
    server = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    
    # Start the server
    server.serve_forever()

<|/ file source=github ext=.py |>