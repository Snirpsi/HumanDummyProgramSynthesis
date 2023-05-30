#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that removes a list of numbers.
    while numbers:
        numbers.remove(numbers.pop())
    print(numbers)

