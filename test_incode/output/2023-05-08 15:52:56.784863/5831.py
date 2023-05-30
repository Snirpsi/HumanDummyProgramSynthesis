#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that adds fruits.
    fruits = input("Enter fruits: ")
    for fruit in fruits.split():
        fruirs.append(fruit)
    print(fruirs)

