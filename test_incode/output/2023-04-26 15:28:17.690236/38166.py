#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input or enumerates numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), Handler)
    
    # Start it
    server.serve_forever()
    
