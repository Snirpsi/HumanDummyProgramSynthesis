#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words and stores all ports. """    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words.sort()
    
    ports = []
    
    for word in words:
        
        ports.append(word.count(' '))
    
    ports.sort()
    
    print(' '.join(words))
    print(' '.join(ports))
    
