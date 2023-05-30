#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        if port == '--help':
            
            print('Usage: %s <port>' % sys.argv[0])
            
        else:
            
            port = int(port)
            
            port2