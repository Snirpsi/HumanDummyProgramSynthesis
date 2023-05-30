#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words and removes fruits. """    
    
    # Create a simple HTTP server
    http_server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Start it
    http_server.serve_forever()

<|/ file source=github ext=.py |>