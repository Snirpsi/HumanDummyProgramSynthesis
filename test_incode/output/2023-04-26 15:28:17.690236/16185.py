#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits and enumerates a list of words. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start the server
    server.serve_forever()
