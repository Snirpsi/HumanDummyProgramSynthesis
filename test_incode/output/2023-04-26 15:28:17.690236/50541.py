#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes all ports and iterates over numbers. """    
    
    ports = range(1,65535)
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('',port))
        sock.listen(1)
        
        print('Listening on port {}'.format(port))
        
        while True:
            
            client, address = sock.accept()
            print('Connected by', address)
            
            client.send('Hello World')
            
            client.close()
            
