#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or returns fruits. """    
    while True:
        fruit = input("Enter fruit name: ")
        if fruit == "exit":
            break
        else:
            print("Adding fruit: " + fruit)
            