#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and opens a port. """    
    
    ports = range(5000, 5999)
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(1)
        
        print('Listening on port ' + str(port))
        
        while True:
            
            conn, addr = sock.accept()
            print('Connected by', addr)
            
            conn.send('Hello, world!\n')
            conn.close()
            
