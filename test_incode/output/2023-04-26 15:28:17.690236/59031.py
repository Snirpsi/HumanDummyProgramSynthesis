#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and returns a port. """    
    
    import sys
    
    ports = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        ports.append(line)
        
    ports.sort()
    
    for port in ports:
        print(port)
    
    sys.exit(0)
    
