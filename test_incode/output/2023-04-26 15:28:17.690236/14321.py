#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or removes all ports. """    
    
    # Create a server
    server = HTTPServer(('', 0), MyHandler)
    
    # Start it
    server.serve_forever()
    
