#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports. """    
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 0))
        sock.listen(1)
        print('Listening on port ' + str(sock.getsockname()[1]))
        
        client, address = sock.accept()
        print('Got connection from ' + str(address[0]))
        client.sendall(b'Hello, world!\n')
        
        client.close()
        sock.close()
        
