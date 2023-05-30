#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers and adds words. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number > 0:
            print(number + number)
        else:
            print(number)
    
