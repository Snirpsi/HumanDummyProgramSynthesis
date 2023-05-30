#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that requests all ports.
    while True:
        port = ports.pop(0)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', port))
        server.listen(1)
        print('Listening on port {}'.format(port))
        client, addr = server.accept()
        print('Connected by', addr)
        while True:
            data = client.recv(1024)
            if not data:
                break
            client.send(data)
        server.close()

