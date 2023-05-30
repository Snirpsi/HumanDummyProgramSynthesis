#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    while True:
        
        sys.stdout.write("Port %d: " % port)
        sys.stdout.flush()
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        
        conn, addr = sock.accept()
        
        conn.send('Hello, world!\n')
        
        conn.close()
        
        port = port + 1
        
