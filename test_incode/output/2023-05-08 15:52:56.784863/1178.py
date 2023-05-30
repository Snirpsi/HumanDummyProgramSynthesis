#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that converts ports.
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', port))
            sock.listen(1)
            print('Listening on port ' + str(port))
            conn, addr = sock.accept()
            print('Connected by', addr)
            conn.send('Hello World')
            conn.close()
            sock.close()

