#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and opens numbers. """    
    while True:
        port = random.randint(1024, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        print('Listening on port %s' % port)
        client, addr = sock.accept()
        print('Got connection from %s' % str(addr))
        while True:
            data = client.recv(1024)
            if not data:
                break
            client.send(data)
        sock.close()
        print('Closing connection')
