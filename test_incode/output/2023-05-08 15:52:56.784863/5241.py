#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that removes numbers.
    numbers = filter(lambda x: x != 3, numbers)
    print(numbers)

