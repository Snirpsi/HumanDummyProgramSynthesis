#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that adds a list of numbers.
    numbers = map(int, input("Enter a number: "))
    numbers = list(numbers)
    numbers.sort()
    print(numbers)

