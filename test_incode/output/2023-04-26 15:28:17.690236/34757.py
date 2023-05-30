#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits and multiplyes words. """    
    while True:
        fruits = input("Enter a fruit name: ")
        fruits = fruits.lower()
        fruits = fruits.split()
        fruits = list(fruits)
        fruits = [fruits[0]] * len(fruits)
        print(*fruits, sep="\n")
