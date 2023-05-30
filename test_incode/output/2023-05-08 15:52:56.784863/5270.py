#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that returns fruits.
    while True:
        fruits = input("Enter a fruit: ")
        if fruits == "quit":
            break
        else:
            print(fruirs.index(fruits))

