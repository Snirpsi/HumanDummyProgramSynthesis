#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that converts numbers.
    #It will take in two arguments: one is the list to convert and the other is the number to convert.
    #It will then return the converted number.
    convert = lambda lst, num: lst[num - 1]
    convert(numbers, 2)
    

