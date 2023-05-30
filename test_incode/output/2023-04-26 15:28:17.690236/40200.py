#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports or removes a list of words. """    
    
    ports = []
    words = []
    
    # Parse command line arguments
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    if len(sys.argv) > 2:
        words = sys.argv[2:]
    
    # Remove all ports
    
    for port in ports:
        
        # Remove port from host
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', int(port)))
        sock.listen(1)
        
        # Remove port from host
        
        sock.close()
        
    # Remove all words
    
    for word in words:
        
        # Remove word from host
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, int(port)))
        sock.send(bytes(word, 'utf-8'))
        sock.close()
        
    # Remove all ports
    
    for port in ports:
        
        # Remove port from host
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, int(port)))
        sock.close()
    
