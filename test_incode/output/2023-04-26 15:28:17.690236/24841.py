#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port and iterates over a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        conn.settimeout(10)
        
        try:
            conn.send(b'OK')
            
            while True:
                buf = conn.recv(1024)
                
                if not buf:
                    break
                
                conn.send(buf)
                
        finally:
            conn.close()
            
        
