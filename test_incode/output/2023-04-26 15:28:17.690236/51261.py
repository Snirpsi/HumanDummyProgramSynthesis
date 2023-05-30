#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or returns fruits. """    
    while True:
        fruits = input("Enter a fruit: ")
        if fruits == 'quit':
            break
        else:
            print("Fruit multiplied by " + str(int(fruits)