#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Run the server
    server.serve_forever()
    
