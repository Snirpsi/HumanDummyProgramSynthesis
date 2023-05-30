#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and prints them
    with open('fruits.txt', 'r') as f:
        for line in f:
            print(line)
    #A function that prints all the fruits in the fruirs list
    for fruit in fruirs:
        print(fruit)

