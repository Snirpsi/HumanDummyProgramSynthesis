#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and prints a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    
    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    
    # Wait for connection
    while True:
        # Accept a connection
        client_socket, address = server_socket.accept()
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(message)
        
        # Receive a message
        message = client_socket.recv(1024)
        
        # Send a message
        client_socket.send(