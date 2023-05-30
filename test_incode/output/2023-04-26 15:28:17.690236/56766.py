#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    # Create a simple server
    server = HTTPServer(("", 80), FruitHandler)
    
    # Start it
    server.serve_forever()
    
