#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits and calculates user input. """    
    
    port = 8080
    
    # Create a server
    server = HTTPServer(('', port), FruitServer)
    
    # Start it
    server.serve_forever()
    
