#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and adds fruits. """    
    
    # Create a socket and bind it to localhost
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    
    # Listen for connections
    sock.listen(1)
    
    # Accept a connection
    client, addr = sock.accept()
    
    # Receive the fruits from the client
    while True:
        data = client.recv(1024)
        if not data:
            break
        
        # Send the fruits back to the client
        client.send(data)
        
    # Close the connection
    client.close()
    
    # Close the socket
    sock.close()
    
