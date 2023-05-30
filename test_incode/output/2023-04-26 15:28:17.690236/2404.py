#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and prints all ports. """    
    import sys
    
    ports = []
    for line in sys.stdin:
        line = line.strip()
        ports.append(int(line))
    
    ports.sort()
    
    for port in ports:
        print('Port {}'.format(port))
        
