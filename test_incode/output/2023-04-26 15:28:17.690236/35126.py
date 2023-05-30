#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or removes all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        ports = sys.argv[1:]
        
    else:
        
        ports = range(0,65535)
        
    for port in ports:
        
        word = ''.join(chr(i) for i in 