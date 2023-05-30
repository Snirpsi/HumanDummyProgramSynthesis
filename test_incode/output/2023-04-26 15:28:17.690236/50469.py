#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words and opens all ports. """    
    
    import sys
    
    ports = []
    
    for port in sys.argv[1:]:
        ports.append(port)
    
    for port in ports:
        
        port = str(port)
        
        try:
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((port, 0))
            
            sock.send(b'Hello')
            
            sock.send(b'World')
            
            sock.close()
            
        except socket.error:
            
            print('Port {} is not open'.format(port))
            
    
