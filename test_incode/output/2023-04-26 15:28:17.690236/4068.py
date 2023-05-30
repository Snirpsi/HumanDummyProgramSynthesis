#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input. """    
    
    number = int(input("Enter a number: "))
    
    product = 1
    
    while number > 0:
        product = product * number
        number = number - 1
    
    print(product)
    
