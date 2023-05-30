#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port and enumerates words. """    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(1)
    
    port = sys.argv[1]
    
    words = []
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    while True:
        line = sock.recv(1024)
        if not line:
            break
        
        line = line.decode('utf-8')
        
        words = line.split(' ')
        
        for word in words:
            print(word)
    
    sock.close()
    
