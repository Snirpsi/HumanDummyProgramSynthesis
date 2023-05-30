#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port or opens words. """    
    
    # Open a port to listen for incoming connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9090))
    server_socket.listen(5)
    
    # Accept the connection and print out the client address.
    while True:
        connection, client_address = server_socket.accept()
        print('Got connection from ', client_address)
        
        # Receive the request from the client.
        data = connection.recv(1024)
        
        # Send the response back to the client.
        connection.send(data)
        
        # Close the connection.
        connection.close()
        
        # 