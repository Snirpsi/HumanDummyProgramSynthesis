#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and prints numbers. """    
    port = int(sys.argv[1])
    
    # Open a socket to listen for connections.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    # Accept connections.
    client, address = sock.accept()
    
    # Receive a message from the client.
    message = client.recv(1024).decode()
    
    # Send the message back to the client.
    client.send(message)
    
    # Close the socket when done.
    client.close()
    
    # Close the server socket.
    sock.close()
    
    # Print the message back to the client.
    print(message)
    
