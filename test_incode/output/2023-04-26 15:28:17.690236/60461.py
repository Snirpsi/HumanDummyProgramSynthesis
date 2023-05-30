#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers or opens all ports. """    
    ports = range(65535)
    
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('127.0.0.1', port))
            sock.listen(1)
            
            print('Listening on port %s' % port)
            
            conn, addr = sock.accept()
            
            print('Connected by', addr)
            
            conn.send('Hello World!')
            
            conn.close()
            
        ports = range(65535)
        
