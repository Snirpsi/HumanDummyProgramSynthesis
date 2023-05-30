#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that enumerates a port.
    def enumerate_port():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(1)
        sock.settimeout(10)
        while True:
            conn, addr = sock.accept()
            conn.settimeout(10)
            conn.sendall(b'Hello, world!')
            conn.close()
    enumerate_port()

