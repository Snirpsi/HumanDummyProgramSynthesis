#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or enumerates all ports. """    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['COM3']
    
    for port in ports:
        
        