#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    # Create the server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start the server
    server.serve_forever()

<|/ file filename=wordserver.py ext=.py |>