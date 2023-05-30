#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port. """    
    while True:
        port = random.randint(10000, 20000)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        print('Listening on port {}'.format(port))
        client, address = sock.accept()
        print('Got connection from {}'.format(address))
        client.send('Hello, world!\n')
        client.close()
