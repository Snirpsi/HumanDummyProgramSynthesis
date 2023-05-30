#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or iterates over fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start it
    server.serve_forever()
    
