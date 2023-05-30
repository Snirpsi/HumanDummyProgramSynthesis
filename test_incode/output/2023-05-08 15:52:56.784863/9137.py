#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that adds a list of numbers.
    for number in numbers:
        print(number)
        numbers.append(number)

