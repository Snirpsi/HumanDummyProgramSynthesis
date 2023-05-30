#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that calculates a list of numbers.
    #The program will then ask the user for input until the user enters 0.
    #The program will then print the list of numbers that have been entered.
    while(True):
        numbers = input("Enter a number: ")
        if(numbers == ""):
            break
        else:
            print(numbers)

