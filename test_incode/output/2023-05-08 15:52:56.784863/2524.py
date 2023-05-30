#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that opens fruits.txt and prints them out
    fruits = open("/Users/james/Desktop/fruits.txt","r")
    for line in fruits:
        print(line)
    fruits.close()

