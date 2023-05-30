#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and removes numbers. """    
    port = int(sys.argv[1])
    
    numbers = []
    
    # Open a socket to listen for connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    
    while True:
        # Accept a connection
        client_socket, address = server_socket.accept()
        
        # Receive the request from the client
        data = client_socket.recv(1024).decode()
        
        # Send the response to the client
        client_socket.send(data.encode())
        
        # Send the response back to the client
        client_socket.send(b'