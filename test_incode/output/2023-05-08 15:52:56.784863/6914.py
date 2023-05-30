#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that removes a list of numbers.
    numbers = list(filter(lambda x: x not in numbers, numbers))
    print(numbers)

