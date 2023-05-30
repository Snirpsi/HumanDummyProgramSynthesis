#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or enumerates fruits. """    
    
    # Create a server that listens on port 80
    server = HTTPServer(("", 80), Fruit)
    
    # Start the server
    server.serve_forever()
    
