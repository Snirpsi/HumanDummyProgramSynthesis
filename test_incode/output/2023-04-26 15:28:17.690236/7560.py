#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and opens a port. """    
    
    port = 1337
    
    while True:
        
        words = [str(x) for x in range(10)]
        
        print('\n'.join(words))
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(1)
        
        print('Listening on port ' + str(port))
        
        client, addr = sock.accept()
        
        print('Connected by', addr)
        
        buf = client.recv(1024)
        
        print('Received', buf)
        
        client.close()
        
        port += 1
        
