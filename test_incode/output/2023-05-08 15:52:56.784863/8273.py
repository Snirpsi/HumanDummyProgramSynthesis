#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that removes a port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    while True:
        client, address = sock.accept()
        print('Got connection from', address)
        client.close()
        sock.close()

