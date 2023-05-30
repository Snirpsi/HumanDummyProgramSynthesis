#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers and returns all ports. """    
    import sys
    
    ports = []
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    
    for port in ports:
        port = int(port)
        
        if port < 1 or port > 65535:
            print('Port must be between 1 and 65535')
            
        else:
            print(port)
    
