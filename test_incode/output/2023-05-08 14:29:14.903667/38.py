#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that opens fruits.txt and prints them one by one
    while True:
        fruir = input("Enter a fruit name: ")
        if fruir in fruirs:
            print(fruir)
        else:
            print("That fruit isn't in the list")

