#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    
    # Create a server
    server = HTTPServer(('', PORT), Handler)
    
    # Start it
    server.serve_forever()

<|/ file ext=.py |>