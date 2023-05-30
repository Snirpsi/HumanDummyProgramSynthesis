#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of numbers. """    
    
    numbers = []
    
    while True:
        number = int(input('Enter a number: '))
        if number in numbers:
            print('This number already exists')
        else:
            numbers.append(number)
            print('Number added')
            
