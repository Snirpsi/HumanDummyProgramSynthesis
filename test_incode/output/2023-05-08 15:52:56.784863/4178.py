#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that enumerates fruits.
    #The function takes an argument 'fruits' which is a list
    #of fruits.
    #The function prints the fruit names in alphabetical order.
    fruits = fruirs
    fruits.sort()
    for fruit in fruits:
        print(fruit)

