#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or opens a port. """    
    
    # Open a port for communication with the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 0))
    server_socket.listen(1)
    
    # Wait for client connection
    client, client_address = server_socket.accept()
    
    # Read all data sent by the client
    data = client.recv(1024)
    
    # Print received data
    print(data)
    
    # Close the connection
    client.close()
    
    # Close the server socket
    server_socket.close()
    
