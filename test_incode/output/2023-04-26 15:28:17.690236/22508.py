#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port. """    
    while True:
        port = random.randint(0,65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        print('Listening on port {}'.format(port))
        client, address = sock.accept()
        print('Connected by', address)
        while True:
            data = client.recv(1024)
            if not data:
                break
            client.send(data)
        client.close()
        sock.close()
