#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or stores a list of words. """    
    
    # Create a socket server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind to the port
    server.bind(('', 0))
    
    # Listen for connections
    server.listen(1)
    
    # Accept a connection
    client, addr = server.accept()
    
    # Print the connected client
    print('Connected by', addr)
    
    # Receive the message
    while True:
        data = client.recv(1024)
        if not data: break
        
        # Send the message back to the client
        client.send(data)
        
    # Close the connection
    client.close()
    
    # Close the server
    server.close()
    
