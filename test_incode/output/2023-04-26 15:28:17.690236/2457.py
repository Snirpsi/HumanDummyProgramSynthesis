#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or adds a port. """    
    
    # Create a server
    server = HTTPServer(('', 8000), FruitHandler)
    
    # Run the server
    server.serve_forever()
    
