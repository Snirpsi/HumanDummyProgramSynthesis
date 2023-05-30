#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that enumerates ports.
    for port in ports:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen(1)
        print('Listening on port {}'.format(port))
        while True:
            client_socket, address = server_socket.accept()
            print('Got connection from {}'.format(address))
            client_socket.send(b'Hello, world!')
            client_socket.close()

