#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers. """    
    
    # Create a server
    server = HTTPServer(('', 80), NumbersHandler)
    
    # Start it
    server.serve_forever()

<|/ file source=github ext=.py |>