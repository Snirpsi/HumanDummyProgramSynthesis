#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and reads it.
    fruits = open("/Users/jonathan/Desktop/fruits.txt","r")
    for line in fruits:
        print(line)
    fruits.close()

