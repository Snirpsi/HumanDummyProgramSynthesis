#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and reads it.
    fruits = open("/Users/james/Desktop/fruits.txt", "r")
    fruit = fruits.read()
    print(fruit)
    fruits.close()

