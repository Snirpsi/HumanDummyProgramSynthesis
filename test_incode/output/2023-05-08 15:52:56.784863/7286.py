#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that removes a port.
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(1)
        client, addr = sock.accept()
        print('Connected by', addr)
        client.send('HTTP/1.1 200 OK\r\n\r\nHello World!')
        client.close()
        sock.close()

