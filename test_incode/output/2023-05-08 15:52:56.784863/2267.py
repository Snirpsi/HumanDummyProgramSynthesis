#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that enumerates numbers.
    while True:
        print(numbers)
        numbers.append(numbers[-1]+1)
        numbers.pop()

