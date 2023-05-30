#!/usr/bin/python3
ports = range(0,65534)
if __name__ == '__main__':
    #A endless loop that opens ports.
    while True:
        port = random.choice(ports)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        print('Listening on port ' + str(port))
        clients = []
        while True:
            client, addr = sock.accept()
            clients.append(client)
            print('Connected by', addr)
            client.send('Hello, world!'.encode())
            client.close()
        for client in clients:
            client.close()

