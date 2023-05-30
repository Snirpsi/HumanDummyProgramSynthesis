#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers and multiplyes user input. """    
    
    numbers = []
    
    while True:
        number = int(input('Enter a number: '))
        numbers.append(number)
        
        if number == 0: break
    
    for number in numbers:
        number *= number
    
    print('The product of all the numbers is {}'.format(number))
    
