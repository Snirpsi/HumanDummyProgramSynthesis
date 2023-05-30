#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and stores all ports. """    
    
    import sys
    
    ports = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        ports.append(int(line))
    
    ports.sort()
    
    for port in ports:
        print(port)
    
