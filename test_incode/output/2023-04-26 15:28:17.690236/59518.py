#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or removes all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port > 0:
            
            ports = range(port)
            
            for port in ports:
                
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                s.bind(('', port))
                
                s.listen(1)
                
                conn, addr = s.accept()
                
                conn.send('Hello World!')
                
                conn.close()
                
        else:
            
            ports = range(0,65535)
            
            for port in ports:
                
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                s.bind(('', port))
                
                s.listen(1)
                
                conn, addr = s.accept()
                
                conn.send('Hello World!')
                
                conn.close()
                
    else:
        
        ports = range(0,65535)
        
        for port in ports:
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            s.bind(('', port))
            
            s.listen(1)
            
            conn, addr = s.accept()
            
            conn.send('Hello World!')
            
            conn.close()
            
            
