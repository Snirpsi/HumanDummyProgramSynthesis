#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits or removes all ports. """    
    while True:
        fruit = input("\nEnter a fruit name: ")
        if fruit == "quit":
            break
        else:
            fruits.remove(fruit)
            print("\nRemoved 