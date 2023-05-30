#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words and opens fruits. """    
    
    # Create a simple server
    server = HTTPServer(('', 8000), WordsHandler)
    
    # Start it
    server.serve_forever()

<|/ file source=github ext=.py filename=server.py |>