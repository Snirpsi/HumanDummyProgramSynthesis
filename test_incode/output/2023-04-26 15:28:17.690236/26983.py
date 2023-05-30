#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits and converts a list of numbers. """    
    
    # Create the server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start the server
    server.serve_forever()

<|/ file ext=.py source=github |>