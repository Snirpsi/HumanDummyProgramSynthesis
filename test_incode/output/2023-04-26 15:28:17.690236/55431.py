#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and enumerates all ports. """    
    
    import sys
    
    words = []
    ports = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words = line.split(' ')
        
        for word in words:
            ports.append(word)
    
    for port in ports:
        print('%s %s' % (port, 