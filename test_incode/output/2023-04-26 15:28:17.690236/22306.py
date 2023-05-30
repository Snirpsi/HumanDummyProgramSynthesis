#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds all ports and iterates over a port. """    
    
    ports = range(65535)
    
    while True:
        
        for port in ports:
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', port))
            sock.listen(1)
            
            print('Listening on port {}'.format(port))
            
            conn, addr = sock.accept()
            
            print('Connected by', addr)
            
            conn.send('Hello, world!')
            
            conn.close()
            
        ports = range(65535)
        
