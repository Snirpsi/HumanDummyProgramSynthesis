#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits or returns a list of numbers. """    
    
    # Initialize a server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start a server
    server.serve_forever()
    
