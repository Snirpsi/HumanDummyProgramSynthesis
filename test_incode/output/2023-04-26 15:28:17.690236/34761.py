#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and calculates all ports. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words = line.split('\t')
        
        if len(words) == 2:
            words.append(words[0])
            
    words.sort()
    
    ports = []
    
    for word in words:
        
        ports.append(word.count(' '))
    
    ports.sort()
    
    print('\n'.join([' '.join(word) for word in words]))
    print('\n'.join([' '.join(port) for port in ports]))
    
