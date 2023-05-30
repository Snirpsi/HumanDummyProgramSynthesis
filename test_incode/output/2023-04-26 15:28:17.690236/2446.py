#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and iterates over words. """    
    
    # Create the server
    server = HTTPServer(("", 80), WordsHandler)
    
    # Start the server
    server.serve_forever()

<|/ file filename=server.py source=github |>