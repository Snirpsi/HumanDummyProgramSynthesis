#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that converts a list of numbers.
    while True:
        numbers = numbers + [numbers.pop()]
        print(numbers)

