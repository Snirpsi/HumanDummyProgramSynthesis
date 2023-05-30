#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that removes a list of numbers.
    numbers_removed = [x for x in numbers if x not in numbers_removed]
    print(numbers_removed)

