#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    
    numbers = open('numbers.txt', 'r')
    
    for line in numbers:
        print(line)
        
    numbers.close()
    
