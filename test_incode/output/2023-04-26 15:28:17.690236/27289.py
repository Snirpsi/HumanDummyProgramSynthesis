#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words and converts all ports. """    
    
    words = []
    ports = []
    
    # Open a port to listen on
    server_address = ('', 8080)
    
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    
    # Accept a connection
    client, client_address = server_socket.accept()
    
    # Receive the request from the client
    message = client.recv(1024)
    
    # Send the response back to the client
    client.send(message)
    
    # Close the connection
    client.close()
    
    # Print the received message
    print(message)
    
    # Close the socket
    server_socket.close()
    
    # Print the list of words
    print(words)
    
    # Print the list of ports
    print(ports)
    
    # Close the socket
    server_socket.close()
    
    # Print the list of words
    print(words)
    
    # Print the list of ports
    print(ports)
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    
    # Close the socket
    server_socket.close()
    