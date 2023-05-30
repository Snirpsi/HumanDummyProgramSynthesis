#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and returns words. """    
    
    ports = []
    
    # Create a server that listens on all available ports
    server = SocketServer.TCPServer(("", 0), MyHandler)
    
    # Listen for connections
    server.serve_forever()
    
    # Close the server
    server.socket.close()
    
    # Print the ports
    for port in ports:
        print("Port {} is open".format(port))
    
    # Print the word
    print("The word 'word' is open")
    
    # Close the server
    server.socket.close()
    
