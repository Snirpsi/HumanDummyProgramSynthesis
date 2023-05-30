#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports and opens a list of words. """    
    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            print('Connected by', addr)
            
            while True:
                
                data = conn.recv(1024)
                
                if not data:
                    break
                
                conn.send(data)
                
            conn.close()
            
        ports = range(1,65535)
        
