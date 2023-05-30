#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits and stores a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start it
    server.serve_forever()
    
