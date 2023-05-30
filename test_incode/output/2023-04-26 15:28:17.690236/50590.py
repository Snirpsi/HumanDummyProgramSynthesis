#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or opens a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0 and number <= 10:
            print(number)
        else:
            print('Invalid number')
    else:
        print('Usage: python 