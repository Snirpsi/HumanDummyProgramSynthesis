#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        if port < 0 or port > 65535:
            print('port must be between 0 and 65535')
            
        else:
            
            