#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    
    # Create a server and a socket to listen to incoming connections
    server = SocketServer.TCPServer(('', 8000), MyHandler)
    
    # Start a thread to handle requests and respond to them
    server.serve_forever()
