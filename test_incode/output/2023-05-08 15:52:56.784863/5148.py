#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that opens fruits.txt and prints all the fruits it finds
    fruits = open("/Users/jonathan/Desktop/fruits.txt","r")
    for line in fruits:
        fruits = line.strip()
        fruits = fruits.split(",")
        for fruit in fruits:
            print(fruit)
    fruits.close()

