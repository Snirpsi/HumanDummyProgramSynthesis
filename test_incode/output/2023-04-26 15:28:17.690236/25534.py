#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    port = int(sys.argv[1])
    
    # Open a socket to the specified port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    # Accept a connection
    client, addr = sock.accept()
    
    # Receive a message from the client
    message = client.recv(1024)
    
    # Close the connection
    client.close()
    
    # Send the message back to the client
    client.send(message)
    
    # Close the socket
    sock.close()
    
    # Close the server
    server.close()
    
    # Close the client
    client.close()
    
