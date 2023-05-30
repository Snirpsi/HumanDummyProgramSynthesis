#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports and opens numbers. """    
    
    ports = [int(port) for port in sys.argv[1:]]
    
    while True:
        for port in ports:
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', port))
            sock.listen(1)
            
            print('Listening on port {}'.format(port))
            
            conn, addr = sock.accept()
            
            print('Connected by', addr)
            
            conn.send('Hello, World!\n')
            
            conn.close()
            
