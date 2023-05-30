#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), NumbersHandler)
    
    # Start it
    server.serve_forever()
    
