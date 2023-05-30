#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and enumerates numbers. """    
    
    # Create a server
    server = HTTPServer(('', 80), FruitServer)
    
    # Start it
    server.serve_forever()

<|/ file ext=.py source=github |>