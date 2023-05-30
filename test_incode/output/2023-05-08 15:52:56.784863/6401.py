#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that enumerates fruits.
    while True:
        fruit = input("Enter a fruit name: ")
        if fruit in fruirs:
            print("The fruit " + fruit + " was found!")
        else:
            print("The fruit " + fruit + " was not found!")
            break

