#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that converts numbers.
    #It reads numbers from stdin and prints them in reverse order.
    #It uses only built-in functions.
    import sys
    numbers = list(map(int, sys.stdin.read().split()))
    print(numbers[::-1])

