#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that adds numbers.
    def addNumbers(numbers):
        sum = 0
        for number in numbers:
            sum += number
        return sum
    print(addNumbers(numbers))

