#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports and enumerates a list of words. """    
    
    # Create a webserver
    server = HTTPServer(('', 0), Handler)
    
    # Start it
    server.serve_forever()
    
    # Stop it
    server.socket.close()
    
