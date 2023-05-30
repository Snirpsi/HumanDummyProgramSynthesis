#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input or adds fruits. """    
    fruits = input("Enter fruits: ")
    fruits = fruits.split()
    for fruit in fruits:
        print(