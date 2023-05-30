#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that removes a port.
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        sock.settimeout(1)
        client, addr = sock.accept()
        print('Connected by', addr)
        client.send('Hello World')
        client.close()
        sock.close()

