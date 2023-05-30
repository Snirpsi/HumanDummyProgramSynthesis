#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that iterates over a list of numbers.
    #It prints the numbers in reverse order.
    for number in numbers:
        print(number)
        number = numbers[::-1]
    print(numbers)

