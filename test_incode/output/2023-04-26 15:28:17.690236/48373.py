#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or stores user input. """    
    
    # Create a server
    server = HTTPServer(("", 8080), RequestHandler)
    
    # Start it
    server.serve_forever()

<|/ file source=github ext=.py |>