#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that converts fruits.txt into lists.
    fruits = open("fruits.txt").readlines()
    fruits = [fruit.strip() for fruit in fruits]
    fruits.sort()
    print(fruits)

