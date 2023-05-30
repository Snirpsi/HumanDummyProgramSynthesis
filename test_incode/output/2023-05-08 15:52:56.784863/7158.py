#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that opens all ports.
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('127.0.0.1', port))
            sock.listen(1)
            sock.settimeout(10)
            conn, addr = sock.accept()
            print('Connected by', addr)
            conn.settimeout(10)
            conn.send('Hello World!')
            conn.close()

