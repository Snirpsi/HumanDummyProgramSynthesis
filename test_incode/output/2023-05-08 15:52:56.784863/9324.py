#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that iterates over fruits.
    for fruit in fruirs:
        print(fruit)
    #A program that prints all the fruits without duplicates.
    fruirs_without_duplicates = list(set(fruirs))
    for fruit in fruirs_without_duplicates:
        print(fruit)

