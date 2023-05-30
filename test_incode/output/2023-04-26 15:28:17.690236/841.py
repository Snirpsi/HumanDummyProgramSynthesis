#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    # Create a server
    server = HTTPServer(('', 80), FruitHandler)
    
    # Run the server
    server.serve_forever()
    
