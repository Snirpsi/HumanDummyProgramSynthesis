#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    server_socket.settimeout(10)
    while True:
        connection, client_address = server_socket.accept()
        connection.sendall(b'HTTP/1.1 200 OK\r\n')
        connection.sendall(b'Content-Type: text/html\r\n')
        connection.sendall(b'Content-Length: 5\r\n')
        connection.sendall(b'\r\n')
        connection.sendall(b'<h1>Hello World!</h1>')
        connection.close()

