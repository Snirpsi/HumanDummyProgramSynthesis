#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits and enumerates a list of numbers. """    
    
    # Create the server
    server = HTTPServer(('', 80), FruitServer)
    
    # Run the server
    server.serve_forever()
    
