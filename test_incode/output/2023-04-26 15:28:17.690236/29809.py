#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports and returns a list of numbers. """    
    ports = [port for port in range(1025)]
    
    while True:
        
        ports.remove(1025)
        
        for port in ports:
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('localhost', port))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            conn.sendall(b'Hello, world!')
            conn.close()
            
        print('Port %d is now closed.' % port)
        
