#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that converts a list of numbers.
    #The program will ask the user for input until they enter a number greater than or equal to 1.
    #The program will then print out the numbers in the list that are not equal to 1.
    while(True):
        number = int(input('Enter a number greater than or equal to 1: '))
        if(number > 1):
            print(numbers)
        else:
            break

