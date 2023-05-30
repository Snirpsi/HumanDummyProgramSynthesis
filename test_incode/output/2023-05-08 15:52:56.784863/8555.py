#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that converts numbers.
    def convert(numbers):
        numbers = numbers.split(',')
        numbers = [int(i) for i in numbers]
        return numbers
    numbers = convert(numbers)
    print(numbers)

