#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that converts a list of numbers.
    def convert(numbers):
        converted = []
        for number in numbers:
            converted.append(str(number))
        return converted
    print(convert(numbers))

