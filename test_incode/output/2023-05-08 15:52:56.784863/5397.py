#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that adds fruits.
    fruits = fruirs + ["mango"]
    #A function that prints the fruits list.
    print(*fruits, sep="\n")

