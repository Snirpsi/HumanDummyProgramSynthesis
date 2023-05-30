#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that opens a port.
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        sock.settimeout(10)
        client, addr = sock.accept()
        print('Got connection from', addr)
        conn.send(b'HTTP/1.1 200 OK\r\n')
        conn.send(b'Content-Type: text/html\r\n')
        conn.send(b'\r\n')
        conn.send(b'<h1>Hello World!</h1>')
        conn.close()

