#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that iterates over fruits.
    while True:
        fruir = input("Enter a fruit: ")
        if fruir in fruirs:
            print(fruir + " is a fruit!")
        else:
            print("That fruit isn't a fruit!")
            break

