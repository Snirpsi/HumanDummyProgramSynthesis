#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port or opens all ports. """    
    while True:
        port = random.randint(0,65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('',port))
        sock.listen(1)
        print('Listening on port %s' % port)
        while True:
            client, addr = sock.accept()
            print('Got connection from %s' % str(addr))
            client.send('Hello World')
            client.close()
