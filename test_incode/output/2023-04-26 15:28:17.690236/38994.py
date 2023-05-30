#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words or multiplyes numbers. """    
    
    words = []
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '' or line == '\n':
            continue
        
        words = line.split()
        
        for word in words:
            numbers.append(int(word))
    
    numbers = map(int, numbers)
    
    for number in numbers:
        number *= 10
    
    for number in numbers:
        print(number)
    
