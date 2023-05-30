#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that requests fruits.
    fruits = input("Enter fruits: ")
    fruits = fruits.split()
    fruits.sort()
    print(fruits)

