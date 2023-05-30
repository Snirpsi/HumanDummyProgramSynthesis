#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that opens a list of numbers.
    numbers = open(sys.argv[1])
    print(numbers)
    #A program that prints the contents of a file.
    numbers = open(sys.argv[1])
    print(numbers.read())

