#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or prints user input. """    
    
    # Create a server
    server = HTTPServer(('', 8000), FruitHandler)
    
    # Start it
    server.serve_forever()

<|/ file filename=server.py ext=.py |>