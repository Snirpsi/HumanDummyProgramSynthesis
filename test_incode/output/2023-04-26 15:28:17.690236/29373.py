#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and enumerates words. """    
    import sys
    import socket
    import select
    
    HOST, PORT = "localhost", 9999
    
    # Create a socket to listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind to the port
    sock.bind((HOST, PORT))
    
    # Listen for incoming connections
    sock.listen(1)
    
    # Create a blocking call to accept connections
    ready, _, _ = select.select([sock], [], [])
    
    # Accept a connection
    connection, client_address = sock.accept()
    
    # Print all ports
    for port in range(1, 65535):
        print("Port {} is listening on {}".format(port, client_address))
    
    # Read a line of text from the client
    data = connection.recv(1024)
    
    # Send the line back to the client
    connection.sendall(data)
    
    # Close the connection
    connection.close()
    
    # Close the socket
    sock.close()
    
    # 