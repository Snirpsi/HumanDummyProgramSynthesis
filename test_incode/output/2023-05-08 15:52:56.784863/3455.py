#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and reads its content
    with open('fruits.txt') as file:
        fruits = file.readlines()
    for fruit in fruits:
        print(fruit)

