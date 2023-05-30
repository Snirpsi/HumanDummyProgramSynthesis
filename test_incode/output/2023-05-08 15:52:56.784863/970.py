#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that returns fruits.
    while True:
        fruits = fruirs
        print("Your fruit is", fruits)
        fruirs = input("Enter another fruit: ")
        if fruirs == "":
            break

