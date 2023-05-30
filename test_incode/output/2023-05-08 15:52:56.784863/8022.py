#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and reads its content
    with open('fruits.txt', 'r') as f:
        fruits = f.readlines()
    #A function that prints all the fruits in the fruits list
    for fruit in fruits:
        print(fruit)

