#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and calculates a list of words. """    
    
    # Create the server
    server = HTTPServer(('', 80), Handler)
    
    # Start it
    server.serve_forever()
    
