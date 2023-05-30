#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port and iterates over a port. """    
    
    port = 5000
    
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        
        print('Listening on port {}'.format(port))
        
        client, addr = sock.accept()
        print('Got connection from {}'.format(addr))
        
        while True:
            data = client.recv(1024)
            if not data:
                break
            
            client.send(data)
        
        sock.close()
        
        client.close()
        
        print('Closing socket')
        
        
