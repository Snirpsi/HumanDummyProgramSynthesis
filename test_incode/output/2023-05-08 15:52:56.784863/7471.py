#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that enumerates a port.
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        client, addr = sock.accept()
        print('Got connection from', addr)
        client.sendall(b'Hello, world!')
        client.close()
        sock.close()

