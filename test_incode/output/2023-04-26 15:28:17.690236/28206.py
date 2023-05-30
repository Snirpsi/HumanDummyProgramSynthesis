#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits and removes a list of words. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "quit":
            break
        fruits.remove(fruit)
        fru