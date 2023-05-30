#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words and opens fruits. """    
    
    # Create a server
    server = HTTPServer(('localhost', 8080), FruitHandler)
    
    # Start it
    server.serve_forever()
    
