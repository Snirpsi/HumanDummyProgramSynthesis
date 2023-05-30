#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or removes all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['COM%s' % (i+1) for i in range(256)]
    
    for port in ports:
        
        try:
            
            