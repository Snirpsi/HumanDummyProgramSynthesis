#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that converts numbers.
    numbers = [int(x) for x in input("Enter numbers: ").split(",")]
    print(numbers)

