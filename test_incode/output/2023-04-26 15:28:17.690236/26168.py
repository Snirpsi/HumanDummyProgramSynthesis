#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    ports_to_remove = [8080, 8081, 8082, 8083, 8084, 8085]
    
    for port in ports_to_remove:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(5)
        
        print('Listening on port {}'.format(port))
        
        while True:
            conn, addr = sock.accept()
            
            print('Connected by', addr)
            
            conn.send('HTTP/1.1 200 OK\r\n\r\n')
            
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                conn.sendall(data)
            
            conn.close()
