#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and converts numbers. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words.append(line)
    
    words.sort()
    
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        numbers.append(int(line))
    
    numbers.sort()
    
    print(" ".join(words))
    print(" ".join(str(n) for n in numbers))
    
