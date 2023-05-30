#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that enumerates a port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        print('Connected by', addr)
        while True:
            data = client.recv(1024)
            if not data:
                break
            print('Received', repr(data))
            client.send(data)
        client.close()

