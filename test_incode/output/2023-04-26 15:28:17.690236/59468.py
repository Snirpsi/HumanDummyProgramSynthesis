#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words. """    
    
    # Create a server
    server = HTTPServer(('', 80), WordCalculator)
    
    # Start it
    server.serve_forever()

<|/ file source=github ext=.py |>