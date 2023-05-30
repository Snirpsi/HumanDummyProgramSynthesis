#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that enumerates a list of numbers.
    def enumerate_numbers(numbers):
        for index, number in enumerate(numbers):
            print(index, number)
    enumerate_numbers(numbers)

