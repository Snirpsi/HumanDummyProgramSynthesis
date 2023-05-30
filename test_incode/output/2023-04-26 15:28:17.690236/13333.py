#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and stores numbers. """    
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        if number not in numbers:
            numbers.append(number)
        else:
            print('Number {} is already in the list'.format(number))
            break
    print('The numbers are: {}'.format(numbers))
    
