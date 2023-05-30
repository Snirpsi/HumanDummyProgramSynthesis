#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that requests numbers.
    #It prints them out in reverse order.
    for number in numbers:
        print(number)
        numbers.remove(number)

