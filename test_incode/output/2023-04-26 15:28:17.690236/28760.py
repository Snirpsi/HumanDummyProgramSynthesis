#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and calculates words. """    
    ports = []
    words = []
    
    for port in range(1, 65535):
        ports.append(port)
        
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        
        while True:
            conn, addr = sock.accept()
            
            conn.send('HTTP/1.1 200 OK\r\nServer: Python-WebServer\r\n\r\n')
            
            word = ''
            
            while True:
                data = conn.recv(1024)
                
                if not data:
                    break
                
                word += data
            
            conn.send(''.join(words))
            conn.close()
            
            words = []
            
