#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that stores a list of numbers.
    #The program will then print all numbers from 1 to 9
    #until the user enters the number 0.
    while(True):
        number = int(input("Enter a number: "))
        if number == 0:
            break
        else:
            print(number)

