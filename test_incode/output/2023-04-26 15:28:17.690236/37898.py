#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    import sys
    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        port = int(port)
        
        ports = [port] * len(ports)
        
        for p in ports:
            print(p)
        
