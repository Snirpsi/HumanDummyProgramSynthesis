#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or opens a port. """    
    
    # Create a server
    server = HTTPServer(("", 8080), FruitHandler)
    
    # Start it
    server.serve_forever()
    
