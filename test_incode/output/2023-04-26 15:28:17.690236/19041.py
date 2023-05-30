#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers and converts numbers. """    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number % 2 == 0:
            print(number)
        else:
            print(number - 1)
    
