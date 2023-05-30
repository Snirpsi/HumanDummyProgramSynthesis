#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that iterates over a port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        print('Connected by', addr)
        data = client.recv(1024)
        if not data:
            break
        client.send(data)
        
    sock.close()

