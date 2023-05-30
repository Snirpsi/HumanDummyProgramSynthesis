#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and enumerates a port. """    
    port = 8000
    
    # Start a server
    server = HTTPServer(("", port), Handler)
    
    # Start a server
    