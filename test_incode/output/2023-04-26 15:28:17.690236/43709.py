#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of numbers. """    
    numbers = [1,2,3,4,5]
    product = numbers[0]
    for number in numbers[1:]:
        product = number * product
    print(product)
