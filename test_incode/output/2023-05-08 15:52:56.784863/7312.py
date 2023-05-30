#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that iterates over all ports.
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        clientSocket, addr = sock.accept()
        print("Connected to", addr)
        while True:
            data = clientSocket.recv(1024)
            if not data:
                break
            clientSocket.send(data)
        clientSocket.close()

