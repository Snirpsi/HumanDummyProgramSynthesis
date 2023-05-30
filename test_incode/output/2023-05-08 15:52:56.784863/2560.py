#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that removes numbers.
    numbers = [x for x in numbers if x not in numbers]
    print(numbers)

