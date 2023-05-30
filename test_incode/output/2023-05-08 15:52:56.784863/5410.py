#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that adds fruits.
    fruits = input("Enter fruits: ")
    fruits = fruits.split()
    fruits = list(fruits)
    fruits.sort()
    for fruit in fruits:
        print(fruit)

