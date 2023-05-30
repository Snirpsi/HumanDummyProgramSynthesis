#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that converts fruits.
    while True:
        fruir = input("Enter a fruit name: ")
        if fruir in fruirs:
            print("The fruit is", fruir)
        else:
            print("The fruit is", fruirs, "not in the list")

