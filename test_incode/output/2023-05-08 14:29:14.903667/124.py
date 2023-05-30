#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that removes a port.
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(1)
        client, addr = sock.accept()
        print('Got connection from', addr)
        client.sendall(b'GET / HTTP/1.0\r\n\r\n')
        data = client.recv(1024)
        print('Received data:', data.decode())
        client.close()
        sock.close()

