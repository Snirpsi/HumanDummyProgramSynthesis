#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of numbers or converts numbers. """    
    numbers = []
    while True:
        try:
            number = int(input('Enter a number: '))
            if number < 0:
                print('Negative numbers not allowed')
            elif number > len(numbers):
                print('Too many numbers')
            else:
                numbers.append(number)
        except ValueError:
            print('Invalid input')
            break
    print('The numbers are:', numbers)

<|/ file ext=.py |>