#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that converts a list of numbers.
    #It will print them in reverse order.
    def reverse(numbers):
        for number in numbers:
            print(number, end=' ')
        reverse(numbers[::-1])
    reverse(numbers)

