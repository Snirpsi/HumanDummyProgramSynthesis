#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and returns words. """    
    
    port = sys.argv[1]
    
    words = []
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', int(port)))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        
        word = ''.join(conn.recv(1024).decode().split())
        
        conn.close()
        
        words.append(word)
        
        print('