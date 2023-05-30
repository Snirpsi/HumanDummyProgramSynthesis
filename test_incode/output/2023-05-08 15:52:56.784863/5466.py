#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that iterates over ports.
    while True:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', ports.pop(0)))
        server.listen(1)
        print('Listening on port {}'.format(ports.pop(0)))
        client, addr = server.accept()
        print('Connected by', addr)
        while True:
            data = client.recv(1024)
            if not data:
                break
            client.send(data)
        client.close()

