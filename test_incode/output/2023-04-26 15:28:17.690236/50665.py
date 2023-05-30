#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and calculates words. """    
    
    port = sys.argv[1]
    
    words = []
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    
    while True:
        conn, addr = sock.accept()
        
        words.append(conn.recv(1024).decode())
        
        conn.close()
    
    sock.close