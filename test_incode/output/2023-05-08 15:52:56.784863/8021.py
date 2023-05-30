#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that iterates over a list of numbers.
    for number in numbers:
        print(number)
    #A function that iterates over a list of numbers and prints them in reverse order.
    for number in reversed(numbers):
        print(number)
    #A function that iterates over a list of numbers and prints them in ascending order.
    for number in sorted(numbers):
        print(number)
    #A function that iterates over a list of numbers and prints them in reverse and ascending order.
    for number in sorted(reversed(numbers)):
        print(number)

