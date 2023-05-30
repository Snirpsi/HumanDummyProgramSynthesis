#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or returns a port. """    
    
    port = int(sys.argv[1])
    
    if port > 0 and port < 65536:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        
        client, addr = sock.accept()
        
        client.send('OK')
        
        client.close()
        
    else:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 0))
        sock.listen(1)
        
        client, addr = sock.accept()
        
        client.send('OK')
        
        client.close()
        
    sock.close()
    
