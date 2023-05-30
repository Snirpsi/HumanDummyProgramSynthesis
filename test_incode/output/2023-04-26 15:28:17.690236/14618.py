#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and iterates over all ports. """    
    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('localhost', port))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            conn.send('Welcome to the 