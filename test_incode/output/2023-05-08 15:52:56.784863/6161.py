#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that removes numbers.
    numbers = filter(lambda x: x != None, numbers)
    print(numbers)

