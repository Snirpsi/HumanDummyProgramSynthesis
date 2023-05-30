#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and iterates over fruits. """    
    while True:
        fruits = input("Enter your favorite fruits: ").split()
        for fruit in fruits:
            print(