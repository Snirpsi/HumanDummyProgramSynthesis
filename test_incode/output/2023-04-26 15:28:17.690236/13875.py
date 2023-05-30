#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and opens all ports. """    
    
    ports = range(65535)
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        
        print('Listening on port ' + str(port))
        
        client, addr = sock.accept()
        print('Connected by', addr)
        
        while True:
            data = client.recv(1024)
            if not data:
                break
            
            client.send(data)
            
        sock.close()
        
        print('Closing socket')
        
