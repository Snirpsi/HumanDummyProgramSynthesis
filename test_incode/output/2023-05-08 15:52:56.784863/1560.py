#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that converts fruits.txt into fruits.csv
    fruits = open("fruits.txt","r")
    fruits.seek(0)
    fruits.truncate()
    fruits.write("fruit,color\n")
    fruits.write(",".join(map(str,fruirs)))
    fruits.close()

