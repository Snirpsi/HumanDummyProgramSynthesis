#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and returns a list of numbers. """    
    
    # Create a server that listens on port 80 and returns a list of numbers
    server = HTTPServer(('', 80), FruitServer)
    
    # Start the server
    server.serve_forever()
    
