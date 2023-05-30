#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    # Create the server
    server = HTTPServer(('', 8000), FruitHandler)
    
    # Run the server
    server.serve_forever()
