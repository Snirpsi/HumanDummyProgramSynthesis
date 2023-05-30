#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and prints words. """    
    port = sys.argv[1]
    
    words = []
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', port))
        s.listen(1)
        
        while True:
            conn, addr = s.accept()
            
            words.append(conn.recv(1024).decode())
            
            conn.close()
            
            print(" ".join(words))
            
            words = []
            
