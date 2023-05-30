#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and stores user input. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start it
    server.serve_forever()
    
