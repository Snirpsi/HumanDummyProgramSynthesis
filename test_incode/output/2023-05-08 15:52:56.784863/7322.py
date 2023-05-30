#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that returns a list of numbers.
    numbers = numbers[:]
    numbers.append(numbers.pop(0))
    print(numbers)

