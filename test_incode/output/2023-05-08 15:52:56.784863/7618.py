#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    while True:
        connection, client_address = server_socket.accept()
        print('Got connection from', client_address)
        connection.send(b'HTTP/1.1 200 OK\r\n')
        connection.send(b'Content-Type: text/html\r\n')
        connection.send(b'\r\n')
        connection.send(b'<html><body>')
        connection.send(b'<h1>Hello World</h1>')
        connection.send(b'</body></html>')
        connection.send(b'\r\n')
        connection.close()

