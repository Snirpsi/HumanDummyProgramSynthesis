#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    # Create a server
    server = HTTPServer(('', 8080), Handler)
    
    # Start it
    server.serve_forever()
    
