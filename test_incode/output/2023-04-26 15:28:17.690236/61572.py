#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports and enumerates user input. """    
    
    ports = enumerate_ports()
    
    while True:
        port = ports.pop()
        
        if port == 'exit':
            break
        
        print('Attempting to connect to port {}...'.format(port))
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((port, 0))
            
            print('Connected to port {}'.format(port))
            
            sock.close()
            
        except socket.error:
            print('Port {} is already in use'.format(port))
            
    print('Done!')
    
