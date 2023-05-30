#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        
        client, addr = sock.accept()
        
        print('Connected by', addr)
        
        while True:
            
            data = client.recv(1024)
            
            if not data:
                break
            
            client.send(data)
            
        client.close()
        
        sock.close()
        
        print('Disconnected')
        
