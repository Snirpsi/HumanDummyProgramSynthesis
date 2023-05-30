#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits or returns words. """    
    fruit = input("Enter a fruit: ")
    fruit = fruit.lower()
    fruits = fruit.split()
    for fruit in fruits:
        print(fruit)
    
