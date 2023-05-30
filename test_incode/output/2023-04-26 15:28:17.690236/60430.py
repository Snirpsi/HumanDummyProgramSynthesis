#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = open('/proc/net/tcp', 'r')
    for line in ports:
        line = line.strip()
        line = line.split(':')
        port = int(line[1])
        
        if port in ports:
            ports.remove(port)
            
    ports = list(set(ports))
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        
        print('Port {} is listening'.format(port))
        
        while True:
            conn, addr = sock.accept()
            
            conn.send('Welcome to 