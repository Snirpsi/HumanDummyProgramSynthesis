#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers and adds a list of words. """    
    
    import sys
    
    words = []
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        numbers.append(int(line))
        
        words.append(line)
    
    numbers.sort()
    
    for number in numbers:
        words.append(" ".join(words[number:]))
    
    print(" ".join(words))
    
