#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that returns a list of numbers.
    numbers = []
    while len(numbers) < 10:
        numbers.append(int(input('Enter a number: ')))
    print(numbers)

