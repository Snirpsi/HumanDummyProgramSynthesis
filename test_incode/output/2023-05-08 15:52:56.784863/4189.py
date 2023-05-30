#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that converts fruits.
    fruits = input("Enter the fruits: ")
    fruits = fruits.split()
    fruits = list(fruits)
    fruits.sort()
    print(fruits)

