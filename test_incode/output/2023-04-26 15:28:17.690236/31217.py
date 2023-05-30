#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits. """    
    while True:
        print("Fruits")
        fruits = input("Enter fruits: ")
        for fruit in fruits.split():
            print(