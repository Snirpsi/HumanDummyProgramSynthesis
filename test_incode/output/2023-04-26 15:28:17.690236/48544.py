#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or iterates over a list of numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Try again.')
            continue
    
    numbers = [x * number for x in range(1, 10)]
    print('The product of {} is {}'.format(number, numbers[0]))
    
