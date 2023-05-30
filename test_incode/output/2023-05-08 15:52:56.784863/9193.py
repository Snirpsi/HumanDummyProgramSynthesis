#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that opens a list of numbers.
    #The program will keep on printing numbers from 1 to 9
    #until the user enters 0.
    while(True):
        number = int(input("Enter a number: "))
        if number == 0:
            break
        else:
            print(number)

