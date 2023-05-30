#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that converts fruits.
    fruits = input("Enter fruits: ")
    fruits = fruits.split()
    for fruit in fruits:
        if fruit in fruirs:
            print(fruit)
        else:
            print("Not a fruit")

