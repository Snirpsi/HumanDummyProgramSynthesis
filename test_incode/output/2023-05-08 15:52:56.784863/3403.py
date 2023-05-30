#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that adds ports.
    while True:
        port = random.randint(0,65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(ports)
        print('Listening on port ' + str(port))
        conn,addr = sock.accept()
        print('Connected by', addr)
        conn.send('Hello World!')
        conn.close()
        sock.close()

