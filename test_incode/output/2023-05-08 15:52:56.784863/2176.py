#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and reads its contents
    with open('fruits.txt') as file:
        fruits = file.readlines()
    #A function that prints all the fruits in the fruirs list
    for fruit in fruirs:
        print(fruit)

