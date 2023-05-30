#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and iterates over all ports. """    
    
    ports = range(65535)
    
    while True:
        for port in ports:
            print('Starting port {}'.format(port))
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('localhost', port))
            sock.listen(1)
            
            print('Listening on port {}'.format(port))
            
            conn, addr = sock.accept()
            
            print('Connected by', addr)
            
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                conn.sendall(data)
            
            conn.close()
            
        print('Stopping server')
        
        