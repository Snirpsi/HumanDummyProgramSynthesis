#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers. """    
    import sys
    
    numbers = sys.argv[1:]
    
    product = 1
    
    for number in numbers:
        product *= number
    
    print(product)
