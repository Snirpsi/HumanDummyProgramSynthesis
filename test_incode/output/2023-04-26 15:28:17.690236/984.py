#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers and calculates fruits. """    
    numbers = []
    fruits = []
    while True:
        number = input('Enter a number: ')
        if number == 'q':
            break
        numbers.append(number)
        fruits.append(calc_fruit(number))
        print('The fruits of number {} are: {}'.format(' '.join(numbers), ', '.join(fruits)))
    print('Thank you for using my program!')

<|/ file source=github ext=.py |>