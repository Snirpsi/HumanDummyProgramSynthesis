#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that stores ports.
    while True:
        for port in ports:
            print(port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            print('Connected by', addr)
            conn.send('Hello World')
            conn.close()
            sock.close()

