#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers and multiplyes a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8000), Handler)
    
    # Start it
    server.serve_forever()
