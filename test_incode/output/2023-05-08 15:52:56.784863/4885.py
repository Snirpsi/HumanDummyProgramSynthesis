#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that calculates numbers.
    #It will ask the user to enter a number and then print out the sum of the numbers.
    number = int(input("Enter a number: "))
    total = 0
    for i in numbers:
        total += i
    print(total)

