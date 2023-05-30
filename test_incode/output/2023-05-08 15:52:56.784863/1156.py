#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    while True:
        client_socket, address = server_socket.accept()
        print("Got connection from ", address)
        
        #A function that sends a message to the client.
        client_socket.sendall('Hello World')
        client_socket.close()

