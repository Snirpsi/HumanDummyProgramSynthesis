#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or opens user input. """    
    while True:
        fruit = input("What is your favorite fruit? ")
        if fruit == "apple":
            print("Apple!")
        elif fruit == "orange":
            print("Orange!")
        elif fruit == "banana":
            print("Banana!")
        elif fruit == "cherry":
            print("Cherry!")
        else:
            print("Oops! That fruit isn't in the list!")
