#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and reads it.
    with open('fruits.txt', 'r') as file:
        fruits = file.readlines()
    #A function that prints all the fruits in the fruits list.
    for fruit in fruits:
        print(fruit)
    #A function that prints all the fruits in the fruits list.
    for fruit in fruits:
        print(fruit)

