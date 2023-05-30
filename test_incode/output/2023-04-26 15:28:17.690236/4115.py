#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    import sys
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number > 10:
            print(number)
        else:
            print('Invalid number')
            
