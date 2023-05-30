#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports. """    
    
    ports = range(1,65535)
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        print('Listening on port {}'.format(port))
        
        while True:
            
            client, address = sock.accept()
            print('Connected by', address)
            
            message = client.recv(1024)
            print('Received message:', message)
            
            client.send('