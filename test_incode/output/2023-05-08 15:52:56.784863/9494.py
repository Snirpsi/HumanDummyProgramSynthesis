#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that opens a list of numbers.
    #The loop will run until the user enters a number that is
    #not in the list.
    while True:
        number = int(input("Enter a number: "))
        if number not in numbers:
            print("That number is not in the list")
        else:
            print(number)
            break
    #The loop will run until the user enters a number that is
    #in the list.
    while True:
        number = int(input("Enter a number: "))
        if number in numbers:
            print(number)
            break
    #The loop will run until the user enters a number that is
    #not in the list.
    while True:
        number = int(input("Enter a number: "))
        if number not in numbers:
            print("That number is not in the list")
        else:
            break

