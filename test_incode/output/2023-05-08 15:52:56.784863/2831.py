#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that opens ports.
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        print('Listening on port {}'.format(port))
        while True:
            conn, addr = sock.accept()
            print('Connected by', addr)
            conn.send('Welcome to the server!')
            conn.close()
            break

