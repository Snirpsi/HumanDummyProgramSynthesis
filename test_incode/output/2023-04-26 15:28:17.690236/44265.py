#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    while True:
        fruits = input("Enter a fruit name: ")
        if fruits == "quit":
            break
        else:
            fruits = fruits.upper()
            fruits = fruits.split()
            for fruit in fruits:
                print(fruit * 