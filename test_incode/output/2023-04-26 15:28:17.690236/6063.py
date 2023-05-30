#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits. """    
    while True:
        print("Add some fruits: ")
        fruits = input("Type fruit names: ").split()
        for fruit in fruits:
            add(fruit)
        print("Done!")
        
def add(