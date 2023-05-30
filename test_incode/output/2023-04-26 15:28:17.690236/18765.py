#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and adds a list of numbers. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words.sort()
    
    for word in words:
        numbers = []
        for number in word:
            numbers.append(int(number))
        
        numbers.sort()
        
        for number in numbers:
            print(number, end=' ')
        print()
    
