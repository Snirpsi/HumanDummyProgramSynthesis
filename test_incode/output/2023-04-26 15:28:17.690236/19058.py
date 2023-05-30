#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers or adds numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number > 0:
            print(number)
        else:
            print('Invalid number')
            
