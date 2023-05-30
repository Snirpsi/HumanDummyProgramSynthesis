#!/usr/bin/python3
if __name__ == '__main__':
    #A function that enumerates user input.
    #The user can input any number of numbers, separated by commas.
    #The function returns the number of numbers the user entered.
    numbers = input("Enter a number separated by commas: ").split(",")
    count = 0
    for number in numbers:
        count = count + 1
    print(count)

