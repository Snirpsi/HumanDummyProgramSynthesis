#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits or converts a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8000), FruitServer)
    
    # Start the server
    server.serve_forever()
    
