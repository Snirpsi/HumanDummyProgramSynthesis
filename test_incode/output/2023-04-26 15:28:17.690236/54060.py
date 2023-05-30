#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and opens all ports. """    
    
    ports = [int(i) for i in sys.argv[1:]]
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        
        print('Listening on port {}'.format(port))
        
        while True:
            conn, addr = sock.accept()
            
            print('Connected by', addr)
            
            conn.send('Hello World!')
            
            conn.close()
            
