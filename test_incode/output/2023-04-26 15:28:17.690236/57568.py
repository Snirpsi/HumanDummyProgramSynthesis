#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words and opens numbers. """    
    
    words = []
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        if line[0] == '#':
            continue
        
        if line[0] == '-':
            continue
        
        words.append(line)
        
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        if line[0] == '-':
            continue
        
        numbers.append(line)
        
    words.sort()
    numbers.sort()
    
    for word in words:
        print(word)
    
    for number in numbers:
        print(number)
        
