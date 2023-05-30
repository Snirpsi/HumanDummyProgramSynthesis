#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that adds ports.
    ports = ports + ports
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(5)
        print('Listening on port {}'.format(port))
        while True:
            conn, addr = sock.accept()
            print('Connected by', addr)
            conn.send('Hello World')
            conn.close()

