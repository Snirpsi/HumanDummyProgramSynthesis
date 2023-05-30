#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that opens a port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(1)
    while True:
        client, address = sock.accept()
        print('Connected by', address)
        data = client.recv(1024)
        if not data:
            break
        client.send(data)
    client.close()

