#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and calculates numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start it
    server.serve_forever()

<|/ file source=github ext=.py |>