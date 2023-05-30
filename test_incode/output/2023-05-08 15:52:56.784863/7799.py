#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that stores a list of numbers.
    #The program will keep on printing the numbers from 1 to 9
    #until the user enters a number greater than 9.
    #The program will then exit the program.
    while True:
        number = int(input("Enter a number between 1 and 9: "))
        if number > 9:
            break
        else:
            print(number)

