#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits and prints user input. """    
    
    # Create a server
    server = HTTPServer(('', 8000), FruitHandler)
    
    # Start it
    server.serve_forever()
    
