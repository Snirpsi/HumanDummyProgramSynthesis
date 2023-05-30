#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    
    numbers = open('numbers.txt','r')
    
    for line in numbers:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        number = int(line)
        
        if number % 2 == 0:
            print(number)
        else:
            print(number * 2)
            
    numbers.close()
    
