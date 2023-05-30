#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers and prints all ports. """    
    
    import sys
    
    ports = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        ports.append(int(line))
        
    for port in ports:
        print(port)
        
