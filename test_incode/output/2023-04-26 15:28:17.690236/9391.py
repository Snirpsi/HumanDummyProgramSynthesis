#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    sock.bind(('localhost', port))
    
    # Listen for connections
    sock.listen(1)
    
    # Accept a connection
    client, addr = sock.accept()
    
    # Receive the message
    message = client.recv(1024)
    
    # Send the message back to the client
    client.send(message)
    
    # Close the connection
    client.close()
    
    # Close the socket
    sock.close()
    
    # Print the message
    print('Message received from client:', message)
    
    # Close the connection
    client.close()
    
    # Close the socket
    sock.close()
    
    # Print the message
    print('Message sent to client:', message)
    
    # Close the connection
    client.close()
    
    # Close the socket
    sock.close()
    
    # Print the message
    print('Program ended')
    
