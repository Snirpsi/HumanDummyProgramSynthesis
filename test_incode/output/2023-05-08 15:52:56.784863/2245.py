#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and prints its content
    with open('fruits.txt') as file:
        for line in file:
            print(line)
    #A function that prints all the fruits from the file fruits.txt
    fruits = open('fruits.txt')
    for line in fruits:
        print(line)
    fruits.close()

