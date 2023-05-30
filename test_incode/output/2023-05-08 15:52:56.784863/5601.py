#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that removes ports.
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', port))
        sock.listen(5)
        print('Listening on port {}'.format(port))
        while True:
            conn, addr = sock.accept()
            print('Connected by', addr)
            conn.setblocking(0)
            conn.send('HTTP/1.1 200 OK\r\n\r\nHello World!')
            conn.close()

