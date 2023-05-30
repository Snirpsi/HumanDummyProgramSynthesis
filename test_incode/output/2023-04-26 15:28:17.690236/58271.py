#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and prints all ports. """    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        if arg == '--ports':
            ports = sys.argv[2:]
            break
    
    for port in ports:
        ports.append(port)
    
    for port in ports:
        print(port)
        
