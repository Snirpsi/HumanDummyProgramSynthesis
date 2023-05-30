#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    sock, addr = sock.accept()
    
    while True:
        
        buf = sock.recv(1024)
        
        if buf:
            
            print('Received:', buf)
            
            sock.sendall(buf)
            
        else:
            
            break
        
    sock.close()
    
