#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that enumerates a port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        print('Got connection from', addr)
        client.send('Hello World!')
        client.close()

