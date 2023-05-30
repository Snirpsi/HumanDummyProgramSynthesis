#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that stores a list of numbers.
    numbers = input("Enter a number: ")
    numbers = [int(i) for i in numbers.split(",")]
    print(numbers)

