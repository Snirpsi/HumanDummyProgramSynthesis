#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words and enumerates numbers. """    
    import sys
    
    words = []
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words = line.split()
        
        for word in words:
            numbers.append(int(word))
    
    numbers = sorted(numbers)
    
    for number in numbers:
        print('%d\t%s' % (number, words[number]))
    
