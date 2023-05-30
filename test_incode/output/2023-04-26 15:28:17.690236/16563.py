#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    
    numbers = open('numbers.txt')
    
    for line in numbers:
        line = line.strip()
        
        if line:
            number = int(line)
            print(number)
    
    numbers.close()
    
