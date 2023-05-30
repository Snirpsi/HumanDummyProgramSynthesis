#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports and enumerates a list of numbers. """    
    
    ports = range(65535)
    
    while True:
        for port in ports:
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            conn.send('