#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports. """    
    
    ports = sys.argv[1:]
    
    ports = ports.split(',')
    
    for port in ports:
        
        port = int(port)
        
        if port > 0 and port < 65535:
            
            