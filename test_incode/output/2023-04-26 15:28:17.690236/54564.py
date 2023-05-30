#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits and adds numbers. """    
    while True:
        fruits = input("Enter fruits: ")
        fruits = fruits.split()
        fruits.remove("apple")
        fruits.remove("banana")
        fruits.remove("cherry")
        fruits.remove("