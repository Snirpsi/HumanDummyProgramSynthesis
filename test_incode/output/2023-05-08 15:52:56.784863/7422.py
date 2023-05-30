#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that opens a list of numbers.
    #The program will ask the user to input the numbers.
    #The program will then print the numbers in reverse order.
    numbers = input("Enter the numbers: ")
    numbers = numbers.split()
    print(numbers)
    print(numbers[::-1])

