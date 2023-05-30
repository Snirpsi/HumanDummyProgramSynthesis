#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and stores fruits. """    
    
    # Create a server
    server = HTTPServer(('', PORT), FruitHandler)
    
    # Start it
    server.serve_forever()
    
