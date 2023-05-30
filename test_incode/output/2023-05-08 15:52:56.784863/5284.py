#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that enumerates fruits.
    fruits = enumerate(fruirs)
    #A function that prints the fruit and its index.
    for fruit, index in fruits:
        print(fruit, index)

