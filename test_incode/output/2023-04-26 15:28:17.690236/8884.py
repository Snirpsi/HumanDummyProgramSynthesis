#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or opens numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        number = int(input('Enter a number: '))
        print(number)
    
