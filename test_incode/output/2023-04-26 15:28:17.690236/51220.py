#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input or opens numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input('Enter a number: '))
    
    print('The number is', number * number)
    
