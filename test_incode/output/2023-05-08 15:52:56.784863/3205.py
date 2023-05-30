#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that iterates over numbers.
    while True:
        print(numbers)
        numbers.append(numbers.pop(0))

