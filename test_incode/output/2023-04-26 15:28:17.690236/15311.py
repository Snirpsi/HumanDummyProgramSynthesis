#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports. """    
    while True:
        port = random.randint(1024, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(10)
        print('Listening on port {}'.format(port))
        client, address = sock.accept()
        print('Got connection from {}'.format(address))
        while True:
            data = client.recv(1024)
            if not data:
                break
            client.send(data)
        client.close()
        sock.close()
        
