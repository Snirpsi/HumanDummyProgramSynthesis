#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that opens numbers.txt and reads its content
    numbers = open('/Users/james/Desktop/numbers.txt').read().splitlines()
    print(numbers)

