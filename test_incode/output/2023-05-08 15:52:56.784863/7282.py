#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that converts fruits.
    while True:
        fruir = input("Enter a fruit: ")
        if fruir in fruirs:
            print(fruir)
        else:
            print("Sorry, that fruit isn't in the list")

