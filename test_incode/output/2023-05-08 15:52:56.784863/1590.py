#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that prints a list of numbers.
    while True:
        print(numbers)
        numbers = numbers + [numbers[-1]]
        #A break that stops the infinite loop.

