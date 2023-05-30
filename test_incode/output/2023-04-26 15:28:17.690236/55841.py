#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    import os
    import socket
    import webbrowser
    
    HOST, PORT = 'localhost', 8080
    
    # Create a socket to listen for connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    
    # Now start a web browser and open a page to receive connections
    webbrowser.open('http://localhost:{}/fruits/'.format(PORT))
    
    # Keep listening for connections
    while True:
        connection, client_address = server_socket.accept()
        print('Got connection from', client_address)
        
        # Receive the fruit 