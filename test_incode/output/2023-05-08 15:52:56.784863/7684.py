#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and prints them out
    with open('fruits.txt') as file:
        for line in file:
            print(line)
    #A function that prints all the fruits from the fruirs list
    for fruit in fruirs:
        print(fruit)

