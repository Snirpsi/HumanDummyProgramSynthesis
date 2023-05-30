#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that adds a list of numbers.
    numbers = list(map(int, input("Enter a number: ")))
    print(numbers)
    numbers = sum(numbers)
    print(numbers)

