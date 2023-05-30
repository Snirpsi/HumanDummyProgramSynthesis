#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and iterates over fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start it
    server.serve_forever()

<|/ file ext=.py |>