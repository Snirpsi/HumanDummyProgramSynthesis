#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers and stores a list of numbers. """    
    
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        if number not in numbers:
            numbers.append(number)
        else:
            print('Number {} already in list'.format(number))
            
        if number == 