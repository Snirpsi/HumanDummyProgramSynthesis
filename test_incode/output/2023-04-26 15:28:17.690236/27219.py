#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    # Create the server
    server = HTTPServer(('', 8080), FruitServer)
    
    # Run the server
    server.serve_forever()
    
