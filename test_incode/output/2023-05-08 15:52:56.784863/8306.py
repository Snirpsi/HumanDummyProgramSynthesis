#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that opens ports.
    while True:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', ports.pop()))
        server_socket.listen(1)
        print('Listening on port %s' % ports.pop())
        server_socket.accept()
        print('Accepted connection from %s' % server_socket.getpeername())
        server_socket.close()

