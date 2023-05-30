#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that opens numbers.txt and prints its contents to stdout
    import sys
    with open(sys.argv[1]) as numbers:
        print(numbers.read())

