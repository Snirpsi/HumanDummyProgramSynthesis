#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and prints them
    with open('fruits.txt') as f:
        for line in f:
            print(line)
    #A function that prints all the fruits from the file fruits.txt
    fruits()

