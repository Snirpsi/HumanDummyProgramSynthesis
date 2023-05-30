#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or stores fruits. """    
    
    # Create a server and bind it to the port 80
    server = HTTPServer(('', 80), FruitHandler)
    
    # Start it
    server.serve_forever()
    
