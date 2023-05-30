#!/usr/bin/python3
if __name__ == '__main__':
    #A function that enumerates user input.
    #The user can input a number or a list of numbers.
    #The function will return the number the user inputted or a list of numbers.
    number = input("Enter a number: ")
    numbers = input("Enter a list of numbers: ")
    
    #The function will return the number the user inputted or a list of numbers.
    return int(number), numbers.split()

