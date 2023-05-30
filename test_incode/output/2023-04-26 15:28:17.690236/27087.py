#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or stores a list of words. """    
    
    ports = range(5000)
    words = []
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        print('Listening on port ' + str(port))
        
        while True:
            conn, addr = sock.accept()
            print('Connected by', addr)
            
            words.append(conn.recv(1024).decode())
            
            conn.close()
            
    sock.close()
    
    print('\n'.join(words))
    
