#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words and converts numbers. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        words = words + line.split(' ')
    
    words.sort()
    
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        numbers = numbers + [int(n) for n in line.split()]
    
    numbers.sort()
    
    for word in words:
        print(word, end=' ')
    
    for number in numbers:
        print(number, end=' ')
    
