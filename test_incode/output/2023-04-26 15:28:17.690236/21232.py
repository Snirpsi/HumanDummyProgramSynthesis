#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    
    # Create the server
    server = HTTPServer(('', 8000), Handler)
    
    # Run the server
    server.serve_forever()

<|/ file source=github filename=server.py |>