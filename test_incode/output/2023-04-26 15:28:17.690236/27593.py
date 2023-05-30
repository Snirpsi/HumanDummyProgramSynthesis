#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits and converts user input. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "quit":
            break
        else:
            fruits.append(fruit)
    fru