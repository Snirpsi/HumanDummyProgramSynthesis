#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words or converts all ports. """    
    
    import sys
    
    if len(sys.argv) == 1:
        ports = range(0,65535)
    else:
        ports = sys.argv[1:]
        
    for port in ports:
        
        print("Port:", port)
        
        