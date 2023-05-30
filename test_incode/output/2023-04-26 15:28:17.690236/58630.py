#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port and stores all ports. """    
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 0))
        sock.listen(1)
        print('Listening on port {}'.format(sock.getsockname()[1]))
        sock.accept()
        print('Accepted connection from {}'.format(sock.getpeername()[1]))
        sock.close