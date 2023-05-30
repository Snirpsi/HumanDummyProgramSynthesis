#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or iterates over a list of words. """    
    
    # Create a server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start it
    server.serve_forever()

<|/ file ext=.py source=github |>