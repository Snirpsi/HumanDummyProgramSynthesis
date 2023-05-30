#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and removes a list of numbers. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words = filter(lambda x: x != '', words)
    
    words = list(set(words))
    
    words.sort()
    
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        numbers.append(line)
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
    
    words.sort()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    words = list(set(words))
