#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that removes a list of numbers.
    numbers = [x for x in numbers if x not in [2,3,4,5,6,7,8,9,10]]
    print(numbers)

