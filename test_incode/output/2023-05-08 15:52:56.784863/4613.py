#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that prints a list of numbers.
    print(numbers)
    #A function that prints a list with one number in each line.
    print(*numbers, sep="\n")

