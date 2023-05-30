#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or calculates a list of numbers. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words = line.split(' ')
        
        if len(words) == 2:
            words.append(words[0])
            
    words.sort()
    
    numbers = []
    
    for word in words:
        numbers.append(int(word))
    
    for number in numbers:
        print(number)
    
