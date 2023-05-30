#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that iterates over fruits.
    while True:
        fruir = input("Enter a fruit name: ")
        if fruir in fruirs:
            print("You entered " + fruir)
        else:
            print("That fruit isn't in the list")

