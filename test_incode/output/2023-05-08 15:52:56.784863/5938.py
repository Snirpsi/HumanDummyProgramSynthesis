#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that stores a list of numbers.
    numbers = input("Enter a number: ")
    print(numbers)
    numbers.append(int(numbers))
    print(numbers)

