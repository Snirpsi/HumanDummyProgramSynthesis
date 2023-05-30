#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers and removes user input. """    
    numbers = []
    while True:
        number = input('Enter a number: ')
        if number == 'done':
            break
        numbers.append(number)
    print('Numbers: ', numbers)
    numbers = numbers.remove