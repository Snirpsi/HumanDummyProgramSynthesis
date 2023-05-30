#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or adds a list of numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid number')
            continue
    
    numbers = []
    while number > 0:
        numbers.append(number)
        number -= 1
    
    print('The numbers 