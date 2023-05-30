#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits and opens a port. """    
    
    # Create a socket to listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    server_address = ('localhost', 9999)
    sock.bind(server_address)
    
    # Listen for incoming connections
    sock.listen(1)
    
    # Accept a connection
    connection, client_address = sock.accept()
    
    # Receive the fruit name
    fruit = connection.recv(1024)
    
    # Send the fruit name back to the client
    connection.sendall(fruit)
    
    # Close the connection
    connection.close()
    
    # 