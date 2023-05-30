#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that adds a port.
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(1)
        print('Listening on port {}'.format(port))
        client, address = sock.accept()
        print('Got connection from', address)
        client.send('Hello World!')
        client.close()

