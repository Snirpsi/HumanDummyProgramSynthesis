#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits and opens user input. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "quit":
            break
        print("You chose " + fruit)
