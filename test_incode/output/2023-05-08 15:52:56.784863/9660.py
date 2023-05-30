#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that calculates numbers.
    while True:
        numbers.append(sum(numbers))
        print(numbers)
        numbers.pop(0)

