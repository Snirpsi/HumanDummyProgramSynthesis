#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that calculates a list of numbers.
    numbers = list(map(int, input().split()))
    print(sum(numbers))

