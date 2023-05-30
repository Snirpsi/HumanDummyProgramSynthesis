#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that iterates over a list of numbers.
    #The function prints the numbers in reverse order.
    def reverse_iterate(numbers):
        for number in numbers:
            print(number, end=' ')
        reverse_iterate(numbers[::-1])
    reverse_iterate(numbers)

