#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that calculates a list of numbers.
    #The program will end when the user enters a number that is
    #not in the list.
    while True:
        number = int(input("Enter a number: "))
        if number not in numbers:
            print("That number is not in the list")
        else:
            numbers.append(number)
            break
    #The program will end when the user enters a number that is
    #not in the list.
    while True:
        number = int(input("Enter a number: "))
        if number in numbers:
            print("That number is in the list")
        else:
            print("That number is not in the list")
            break

