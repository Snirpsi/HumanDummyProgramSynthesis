#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), Handler)
    
    # Start it
    server.serve_forever()

<|/ file source=github filename=server.py |>