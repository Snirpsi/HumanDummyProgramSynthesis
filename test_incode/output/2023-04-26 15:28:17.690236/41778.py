#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port. """    
    while True:
        port = random.randint(10000, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        sock.settimeout(10)
        client, addr = sock.accept()
        print('Got connection from', addr)
        client.send('Hello World!')
        client.close()
