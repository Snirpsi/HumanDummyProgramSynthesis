#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of numbers and prints user input. """    
    numbers = [int(i) for i in input('Enter numbers: ').split()]
    
    product = 1
    for number in numbers:
        product *= number
    
    print('The product is', product)
