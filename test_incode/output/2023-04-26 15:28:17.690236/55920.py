#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and opens all ports. """    
    
    ports = []
    
    # Open all ports
    for port in range(1, 65535):
        ports.append(port)
        
    # Enumerate all ports
    for port in ports:
        
        # Open port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        
        # Print port
        print('Port {} is open'.format(port))
        
        # Accept connection
        conn, addr = sock.accept()
        
        # Print connection
        print('Connection from {}'.format(addr))
        
        # Close connection
        conn.close()
        
    # Close all ports
    for port in ports:
        sock.close()
        
