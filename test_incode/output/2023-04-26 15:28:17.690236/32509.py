#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and stores fruits. """    
    
    # Create the server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start it
    server.serve_forever()
