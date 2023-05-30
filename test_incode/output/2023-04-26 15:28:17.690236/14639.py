#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports. """    
    
    ports = []
    
    ports.append( ('tcp', 80, 80) )
    ports.append( ('tcp', 8080, 80) )
    ports.append( ('tcp', 8081, 80) )
    ports.append( ('tcp', 8082, 80) )
    ports.append( ('tcp', 8083, 80) )
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind( port )
        sock.listen(10)
        
        print('Listening on port %s' % port)
        
        while True:
            
            client, addr = sock.accept()
            
            print('Connected by', addr)
            
            client.sendall('Hello World!')
            
            client.close()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
