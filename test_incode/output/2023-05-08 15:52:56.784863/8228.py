#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that opens a port.
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        sock.settimeout(1)
        client, address = sock.accept()
        print('Connected by', address)
        client.send('Hello, world!'.encode())
        client.close()
        sock.close()

