#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that requests numbers.
    #The program prints the numbers in reverse order.
    numbers = input("Enter numbers: ")
    numbers = list(map(int, numbers.split()))
    print(numbers[::-1])

