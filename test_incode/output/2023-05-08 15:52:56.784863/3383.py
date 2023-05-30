#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that opens fruits.txt and prints out the fruit names in it
    fruits = open("/Users/james/Desktop/fruits.txt","r").read().splitlines()
    for fruit in fruits:
        print(fruit)

