#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that removes fruits.
    fruits = input("Enter fruits: ")
    for fruit in fruits:
        if fruit not in fruirs:
            print(fruit)

