#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port and returns a port. """    
    while True:
        port = random.randint(10000, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        print('Listening on port {}'.format(port))
        sock, addr = sock.accept()
        print('Got connection from {}'.format(addr))
        sock.send('Hello, world!')
        sock.close()
