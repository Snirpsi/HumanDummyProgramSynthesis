#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that iterates over fruits.
    while True:
        fruits = input("Enter a fruit name: ")
        if fruits == "":
            break
        else:
            print(fruits)

