#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers and iterates over fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_iter = iter(fruits)
    while True:
        try:
            number = next(fruits_iter)
            print(number)
        except StopIteration:
            break
    
