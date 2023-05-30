#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input and adds all ports. """    
    import sys
    
    ports = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        ports.append(line)
        
    ports = list(set(ports))
    
    for port in ports:
        print(port)
        
