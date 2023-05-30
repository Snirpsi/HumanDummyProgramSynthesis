#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that stores numbers.
    while True:
        numbers.append(numbers.pop(0))
        print(numbers)

