#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that converts numbers.
    #It takes two arguments: one is the number to be converted
    #and the other is the base of the conversion.
    import sys
    number = int(sys.argv[1])
    base = int(sys.argv[2])
    number = number * base
    print(number)

