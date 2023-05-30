#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and removes a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8000), FruitRemover)
    
    # Start it
    server.serve_forever()
