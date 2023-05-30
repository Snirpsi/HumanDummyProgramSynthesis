#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that adds a list of numbers.
    def add(numbers):
        total = 0
        for num in numbers:
            total += num
        return total
    print(add(numbers))

