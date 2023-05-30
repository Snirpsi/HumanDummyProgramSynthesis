#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    
    # Create a server
    server = HTTPServer(('', 8080), Handler)
    
    # Start the server
    server.serve_forever()

<|/ file ext=.py filename=