#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that returns fruits.
    while True:
        fruir = input("Enter a fruit: ")
        if fruir in fruirs:
            print(fruir)
        else:
            print("Sorry, that fruit is not in the list")

