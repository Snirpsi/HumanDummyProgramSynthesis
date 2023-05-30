#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8000), FruitHandler)
    
    # Start it
    server.serve_forever()

<|/ file source=github filename=fruit