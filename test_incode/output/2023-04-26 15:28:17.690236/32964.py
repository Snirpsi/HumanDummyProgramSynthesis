#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or stores fruits. """    
    
    # Initialize a server
    server = HTTPServer(("", 80), FruitHandler)
    
    # Start a server
    server.serve_forever()
    
