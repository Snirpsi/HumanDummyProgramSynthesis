#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port. """    
    port = int(sys.argv[1])
    
    # Create a socket and bind it to port 8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    
    # Listen for connections
    sock.listen(1)
    
    # Accept a connection
    client, address = sock.accept()
    
    # Receive the message
    message = client.recv(1024)
    
    # Send the message back to the client
    client.send(message)
    
    # Close the connection
    client.close()
    
    # Close the socket
    sock.close()
    
