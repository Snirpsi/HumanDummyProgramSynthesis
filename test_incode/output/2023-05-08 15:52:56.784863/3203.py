#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that calculates numbers.
    numbers = map(int, input("Enter numbers: ").split())
    print(sum(numbers))

