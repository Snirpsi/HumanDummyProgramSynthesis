#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port or opens all ports. """    
    while True:
        port = random.randint(1, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        print('Listening on port {}'.format(port))
        
        client, addr = sock.accept()
        print('Connected by', addr)
        
        buf = client.recv(1024)
        while buf:
            client.send(buf)
            buf = client.recv(1024)
        
        client.close()
        sock.close()
        
