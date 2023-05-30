#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words and converts numbers. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
    words.sort()
    
    for word in words:
        
        number = int(word)
        
        if number < 0:
            continue
        
        if number % 2 == 0:
            print(word)
        else:
            print(word + '