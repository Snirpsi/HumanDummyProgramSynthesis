#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words and opens a list of numbers. """    
    
    import sys
    
    words = []
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line or line[0] == '#':
            continue
        
        words = line.split()
        
        for word in words:
            numbers.append(word)
    
    numbers.sort()
    
    for number in numbers:
        print(number)
    
