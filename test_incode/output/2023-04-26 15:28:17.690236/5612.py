#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    # Create a server
    server = HTTPServer(("", 8080), Handler)
    
    # Start it
    server.serve_forever()

<|/ file ext=.py filename=server.py |>