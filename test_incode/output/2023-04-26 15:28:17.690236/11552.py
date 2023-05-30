#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8000), FruitServer)
    
    # Start it
    server.serve_forever()
    
