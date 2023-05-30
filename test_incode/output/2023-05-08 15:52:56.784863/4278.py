#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that adds a port.
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.accept()
        print('Listening on port {}'.format(port))
        sock.close()

