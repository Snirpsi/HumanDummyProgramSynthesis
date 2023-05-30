#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and stores a list of words. """    
    
    ports = [int(port) for port in sys.argv[1:]]
    
    words = []
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        
        while True:
            
            conn, addr = sock.accept()
            
            conn.send('HTTP/1.1 200 OK\r\n\r\n')
            
            words.append(conn.recv(1024).decode())
            
            conn.close()
            
    