#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits and stores fruits. """    
    while True:
        fruits = input("Enter a fruit: ")
        fruits = fruits.lower()
        fruits = fruits.split()
        fruits = list(fruits)
        fruits = [int(x) for x in fruits]
        fruits = [x*