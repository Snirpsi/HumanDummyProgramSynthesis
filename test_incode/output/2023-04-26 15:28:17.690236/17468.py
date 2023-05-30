#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input and stores numbers. """    
    
    number1 = int(input('Enter first number: '))
    number2 = int(input('Enter second number: '))
    
    number3 = number1 * number2
    
    print('The product of {0} and {1} is {2}'.format(number1, number2, number3))
    
