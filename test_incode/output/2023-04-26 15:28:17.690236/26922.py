#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    
    ports = open('/proc/net/tcp','r').read().splitlines()
    
    for port in ports:
        
        port = int(port)
        
        if port == 80:
            
            print('Port 80')
            
        elif port == 443:
            
            print('Port 443')
            
        else:
            
            print('Port 