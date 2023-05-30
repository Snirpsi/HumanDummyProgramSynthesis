#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that removes ports.
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', port))
        sock.listen(5)
        while True:
            conn, addr = sock.accept()
            conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            conn.settimeout(10)
            conn.sendall(b'HTTP/1.1 200 OK\r\nServer: Apache\r\nConnection: close\r\n\r\nHello World!')
            conn.close()
            sock.close()

