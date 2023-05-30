#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    # Create a server and a socket to listen for connections.
    server = SocketServer.TCPServer(("", PORT), Handler)
    
    # Start 