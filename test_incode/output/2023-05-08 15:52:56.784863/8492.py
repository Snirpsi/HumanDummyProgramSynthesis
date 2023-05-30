#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that iterates over a port.
    #The port is opened and closed at the end.
    while(True):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        client, addr = sock.accept()
        print('Connected by', addr)
        
        #A function that sends a message to the client.
        #The client is opened and closed at the end.
        def send_message():
            message = input('Enter a message:')
            client.send(message)
        
        #A function that receives a message from the client.
        #The client is opened and closed at the end.
        def receive_message():
            message = client.recv(1024)
            print('Received', message)
        
        #A function that closes the client.
        #The client is opened and closed at the end.
        def close_client():
            client.close()
        
        #A function that closes the server.
        #The server is opened and closed at the end.
        def close_server():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit_and_exit():
            sock.close()
        
        #A function that closes the socket and exits.
        #The socket is opened and closed at the end.
        def close_socket_and_exit_and_exit_and_

