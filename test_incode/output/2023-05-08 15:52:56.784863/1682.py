#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that opens all ports.
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            print('Listening on port {}'.format(port))
            conn, addr = sock.accept()
            print('Connected by', addr)
            conn.sendall(b'Hello, world!')
            conn.close()

