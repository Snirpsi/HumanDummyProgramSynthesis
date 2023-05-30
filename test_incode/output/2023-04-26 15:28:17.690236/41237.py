#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port or calculates a list of words. """    
    
    # Create a socket to listen on port 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    
    # Create a socket to receive messages from the server
    client_socket, address = server_socket.accept()
    
    # Create a socket to send messages to the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 8080))
    
    # Create a socket to receive messages from the server
    client_socket, address = server_socket.accept()
    
    # Create a socket to send messages to the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 8080))
    
    # Create a socket to receive messages from the server
    client_socket, address = server_socket.accept()
    
    # Create a socket to send messages to the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 8080))
    
    # Create a socket to receive messages from the server
    client_socket, address = server_socket.accept()
    
    # Create a socket to send messages to the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 8080))
    
    # Create a socket to receive messages from the server
    client_socket, address = server_socket.accept()
    
    # Create a socket to send messages to the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 8080))
    
    # Create a socket to receive messages from the server
    client_socket, address = server_socket.accept()
    
    # Create a socket to send messages to the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 8080))
    
    # Create a socket to receive messages from the server
    client_socket, address = server_socket.accept()
    
    # Create a socket to send messages to the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 8080))
    
    # Create a socket to receive messages from the server
    client_socket, address = server_socket.accept()
    
    # Create a socket to send messages to the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 8080))
    
    # Create a socket to receive messages from the server
    client_socket, address = server_socket.accept()
    
    # Create a socket to send messages to the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost