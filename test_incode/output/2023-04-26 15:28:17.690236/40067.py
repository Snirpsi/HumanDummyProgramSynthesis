#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers or prints numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        print(number)
    else:
        print('No number given.')
    
