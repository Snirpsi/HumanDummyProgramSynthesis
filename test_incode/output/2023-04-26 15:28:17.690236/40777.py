#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers or returns words. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            print(number * 'x')
        else:
            print('0')
    else:
        print('Usage: python multiply