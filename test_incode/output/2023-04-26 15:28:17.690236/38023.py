#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words and iterates over all ports. """    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('127.0.0.1', port))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                words = data.split()
                
                for word in words:
                    conn.send(word)
                    
                conn.close()
                
            conn.close()
            
        ports.remove(port)
        
        print('Port %d is now closed.' % port)
        
        
