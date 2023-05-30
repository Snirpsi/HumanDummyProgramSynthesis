#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        if port > 0 and port < 65535:
            
            ports.add(port)
            
    print('\n'.join(ports))
    
