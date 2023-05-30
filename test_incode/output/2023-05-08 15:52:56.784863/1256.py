#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that opens fruits.txt and prints them one by one
    while True:
        fruits = open("/Users/jonathan/Desktop/fruits.txt", "r")
        for line in fruits:
            print(line)
        fruits.close()
        break

