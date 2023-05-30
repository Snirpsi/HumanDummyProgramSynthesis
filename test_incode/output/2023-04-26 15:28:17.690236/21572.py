#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        multiplier = int(sys.argv[1])
    else:
        multiplier = 1
    
    multiplied_number = multiplier * int(input('Enter a number: '))
    print('The multiplied number is', multiplied_number)
    
