#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    while True:
        fruits = input("Enter the fruits: ")
        fruits = fruits.split()
        fruits.sort()
        print("The fruits are:")
        for fruit in fruits:
            print(