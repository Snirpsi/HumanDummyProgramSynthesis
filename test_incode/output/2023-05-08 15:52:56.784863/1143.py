#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that requests fruits.
    fruits = input("Enter fruits: ")
    for fruit in fruits.split():
        if fruit not in fruirs:
            print("Sorry, {} is not in our list of fruits!".format(fruit))

