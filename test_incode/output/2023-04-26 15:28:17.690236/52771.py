#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    # Create a server
    server = HTTPServer(('localhost', 8000), FruitHandler)
    
    # Start it
    server.serve_forever()
