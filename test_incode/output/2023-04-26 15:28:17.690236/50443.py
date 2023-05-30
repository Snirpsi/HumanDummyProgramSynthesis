#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and stores numbers. """    
    port = sys.argv[1]
    port = int(port)
    
    ports = [port]
    
    while(True):
        
        port = ports.pop(0)
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        
        while(True):
            
            sock, addr = sock.accept()
            
            ports.append(port)
            
            sock.close()
            
