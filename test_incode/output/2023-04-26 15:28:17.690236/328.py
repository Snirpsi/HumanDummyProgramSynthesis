#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port. """    
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 0))
        sock.listen(1)
        sock.settimeout(10)
        conn, addr = sock.accept()
        print('Connected by', addr)
        conn.send('Hello, world!