#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and opens a port. """    
    
    ports = range(65535)
    
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('127.0.0.1', port))
            sock.listen(1)
            
            print('Opened port {}'.format(port))
            
            sock.close()
            
