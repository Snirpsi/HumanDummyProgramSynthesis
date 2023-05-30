#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that converts a list of numbers.
    def convert(numbers):
        numbers_converted = []
        for number in numbers:
            numbers_converted.append(number*2)
        return numbers_converted
    print(convert(numbers))

