#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and removes a port. """    
    
    # Create a server and bind it to the port 8000
    server = HTTPServer(('', 8000), FruitHandler)
    
    # Start it
    server.serve_forever()
