#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits and removes fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start it
    server.serve_forever()

<|/ file ext=.py source=github |>