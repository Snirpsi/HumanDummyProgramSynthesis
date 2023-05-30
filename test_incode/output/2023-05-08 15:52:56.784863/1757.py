#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that opens a list of numbers.
    #It will print them out in reverse order.
    def reverse_list(numbers):
        for number in numbers:
            print(number, end=' ')
        reverse_list(numbers[::-1])
    reverse_list(numbers)

