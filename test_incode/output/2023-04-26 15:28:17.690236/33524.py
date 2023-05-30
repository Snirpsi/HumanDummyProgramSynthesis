#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    ports_to_remove = []
    
    for port in range(0, 65535):
        ports_to_remove.append(port)
    
    for port in ports_to_remove:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(1)
        
        print('Listening on port ' + str(port))
        
        while True:
            conn, addr = sock.accept()
            
            print('Connected by', addr)
            
            conn.send('HTTP/1.1 200 OK\r\nServer: Apache\r\n\r\nHello World!\r\n\r\n')
            
            conn.close()
            
            print('Closing connection')
            
            
