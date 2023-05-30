#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers and prints fruits. """    
    
    # Create a server
    server = HTTPServer(("", 80), FruitHandler)
    
    # Start it
    server.serve_forever()

<|/ file source=github ext=.py |>