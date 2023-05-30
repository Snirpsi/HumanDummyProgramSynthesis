#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that converts a list of numbers.
    #The loop will continue until a user enters a number greater than the length of numbers.
    #The program will then print out the list with the number the user entered.
    while(True):
        number = int(input("Enter a number: "))
        if(number > len(numbers)):
            print("The list was too long.")
        else:
            print(numbers[number-1])

