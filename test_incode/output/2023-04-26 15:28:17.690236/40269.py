#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits or calculates user input. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitServer)
    
    # Start it
    server.serve_forever()
    
