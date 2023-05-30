#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    # Start the server
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Start the server
    server.serve_forever()

<|/ file ext=.py |>