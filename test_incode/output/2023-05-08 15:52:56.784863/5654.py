#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that adds a list of numbers.
    def addNumbers(numbers):
        total = 0
        for number in numbers:
            total = total + number
        return total
    print(addNumbers(numbers))

