#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that adds fruits.
    fruits = input("Enter fruits: ")
    fruits = fruits.split()
    for fruit in fruits:
        if fruit not in fruirs:
            fruirs.append(fruit)
    print("The fruits are", fruirs)

