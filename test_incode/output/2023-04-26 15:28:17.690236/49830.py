#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and calculates numbers. """    
    
    # Create the server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start the server
    server.serve_forever()
    
