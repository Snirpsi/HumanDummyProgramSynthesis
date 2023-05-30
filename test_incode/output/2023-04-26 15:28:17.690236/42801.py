#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or stores a list of numbers. """    
    
    # Create the webserver
    server = HTTPServer(('', 8080), Handler)
    
    # Start the webserver
    server.serve_forever()
