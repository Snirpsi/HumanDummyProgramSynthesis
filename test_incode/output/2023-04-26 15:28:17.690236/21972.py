#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    # Create a server
    server = HTTPServer(('localhost', 8080), Handler)
    
    # Run the server
    server.serve_forever()

<|/ file ext=.py |>