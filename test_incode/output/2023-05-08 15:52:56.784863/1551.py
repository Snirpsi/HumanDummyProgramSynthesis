#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that adds numbers.
    numbers = list(map(int, input().split()))
    print(sum(numbers))

