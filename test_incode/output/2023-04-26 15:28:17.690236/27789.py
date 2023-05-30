#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    while True:
        print("Multiplying fruits...")
        fruits = input("Enter a fruit: ")
        fruits = fruits.lower()
        fruits = fruits.split()
        fruits = list(fruits)
        fruits = [int(x) for x in fruits]
        fruits = [x*