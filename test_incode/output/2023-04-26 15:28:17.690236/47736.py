#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers. """    
    
    numbers = []
    
    while True:
        try:
            number = int(input('Enter a number: '))
            numbers.append(number)
        except ValueError:
            print('Invalid input')
        else:
            break
    
    print('The numbers 