#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers. """    
    
    numbers = open('numbers.txt', 'r')
    
    for line in numbers:
        line = line.strip()
        
        if line == '':
            continue
        
        number = int(line)
        
        if number % 2 == 0:
            print(number, end=' ')
        else:
            print(number, end=' ')
        
        numbers.close()
        
    numbers.close()
    
    
