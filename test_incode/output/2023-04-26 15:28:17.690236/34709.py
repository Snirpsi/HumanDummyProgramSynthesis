#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and returns all ports. """    
    
    ports = []
    
    # Open a socket to listen on all available ports
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 0))
    server_socket.listen(1)
    
    # Accept connections from clients
    while True:
        # Wait for connection
        client_socket, client_addr = server_socket.accept()
        
        # Receive data from client
        data = client_socket.recv(1024)
        
        # Send data to client
        client_socket.send(data)
        
        # Close connection
        client_socket.close()
        
        # Print all ports
        for port in ports:
            print(port)
        
        # Close socket
        client_socket.close()
        
        # Wait for another client
        client_socket, client_addr = server_socket.accept()
        
    # Close socket
    server_socket.close()
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Close socket
    server_socket.close()
    
    # Close server
    server_socket.close()
    
    # Close ports
    for port in ports:
        port.close()
    
    # Close socket
    server_socket.close()
    
    # Close all ports
    for port in ports:
        port.close()
    
    # Close socket
    server_socket.close()
    
    # Close all sockets
    for sock in (server_socket, client_socket):
        sock.close()
    
    # Close all ports
    for port in ports:
        port.close()
    
    # Close all sockets
    for sock in (server_socket, client_socket):
        sock.close()
    
    # Close all ports
    for port in ports:
        port.close()
    
    # Close all sockets
    for sock in (server_socket, client_socket):
        sock.close()
    
    # Close all ports
    for port in ports:
        port.close()
    
    # Close all sockets
    for sock in (server_socket, client_socket):
        sock.close()
    
    # Close all ports
    for port in ports:
        port.close()
    
    # Close all sockets
    for sock in (server_socket, client_socket):
        sock.close()
    
    # Close all ports
    for port in ports:
        port.close()
    
    # Close all sockets
    for sock in (server_socket, client_socket):
        sock.close()
    
    # Close all ports
    for port in ports:
        port.close()
    
    # 