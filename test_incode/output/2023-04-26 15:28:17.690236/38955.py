#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers and iterates over user input. """    
    
    number1 = int(input('Enter first number: '))
    number2 = int(input('Enter second number: '))
    
    total = 0
    
    for number in range(number1, number2):
        total += number
    
    print(total)
    
