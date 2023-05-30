#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that removes a port.
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        port = sock.getsockname()[1]
        sock.close()
        print('Port {} is closed.'.format(port))

