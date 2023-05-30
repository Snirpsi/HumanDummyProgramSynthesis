#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input and adds a list of numbers. """    
    
    numbers = []
    while True:
        try:
            number = int(input('Enter a number: '))
            numbers.append(number)
        except ValueError:
            print('Invalid input')
        else:
            break
    
    print('The list of numbers is: ', numbers)
    
