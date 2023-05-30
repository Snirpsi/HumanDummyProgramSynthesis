#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port and stores a list of words. """    
    
    port = 5000
    words = []
    
    while True:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        
        print('Listening on port {}'.format(port))
        
        client, addr = sock.accept()
        
        print('Connected by', addr)
        
        while True:
            
            message = client.recv(1024)
            
            if message:
                
                words = message.split()
                
                print('Received message:', message)
                
                client.send(b'OK')
                
            else:
                
                break
        
        sock.close()
        
        print('Closing socket')
        
        client.close()
        
        print('Closing connection')
        
