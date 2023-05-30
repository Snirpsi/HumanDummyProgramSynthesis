#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers and iterates over numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()

<|/ file filename=server.py |>