#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers and opens fruits. """    
    
    # Create a server
    server = HTTPServer(('', 80), FruitHandler)
    
    # Start it
    server.serve_forever()

<|/ file source=github dstars=1 |>