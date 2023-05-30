#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input. """    
    
    import sys
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        line = line.split()
        
        if len(line) < 2:
            continue
        
        number = line[0]
        
        if number == '':
            continue
        
        number = int(number)
        
        if number % 2 == 0:
            print(number)
        else:
            print(number * -1)
        
