#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that returns fruits.
    while True:
        fruir = input("Enter a fruit name: ")
        if fruir in fruirs:
            print(fruir)
        else:
            print("That fruit is not in the list")

