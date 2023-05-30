#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that converts ports.
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.sendall(b'HTTP/1.1 200 OK\r\n')
            conn.sendall(b'Server: Python\r\n')
            conn.sendall(b'Content-Type: text/html\r\n')
            conn.sendall(b'\r\n')
            conn.sendall(b'Hello World!\r\n')
            conn.close()

