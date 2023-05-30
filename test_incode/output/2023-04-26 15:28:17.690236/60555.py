#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and calculates a list of words. """    
    
    # Open a port on which to listen
    server_address = ('localhost', 8000)
    
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind to the port
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    
    # Accept a connection
    connection, client_address = server_socket.accept()
    
    # Receive the file name
    filename = connection.recv(1024)
    
    # Send the file name
    connection.send(filename.encode())
    
    # Receive the file content
    content = connection.recv(1024)
    
    # Send the file content
    connection.send(content.encode())
    
    # Close the connection
    connection.close()
    
    # Close the socket
    server_socket.close()

<|/ file ext=.py |>