#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or enumerates user input. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        if number.isdigit():
            print(int(number))
        else:
            print(number)
            
