#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port and opens all ports. """    
    while True:
        port = random.randint(1, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(5)
        print('Listening on port {}'.format(port))
        while True:
            conn, addr = sock.accept()
            print('Connected by', addr)
            conn.sendall(b'Hello, world!')
            conn.close()
