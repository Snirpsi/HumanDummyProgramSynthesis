#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers and enumerates fruits. """    
    
    # Create a server
    server = HTTPServer(('', 8080), FruitServer)
    
    # Start it
    server.serve_forever()
    
