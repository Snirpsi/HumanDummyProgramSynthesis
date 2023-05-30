#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports or enumerates a port. """    
    
    # Create a socket server
    server = SocketServer(("", PORT), MyHandler)
    
    # Start server
    server.serve_forever()
    
