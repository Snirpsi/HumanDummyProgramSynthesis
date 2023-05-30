#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits and returns user input. """    
    while True:
        fruit = input("Enter a fruit name: ")
        if fruit == "quit":
            break
        else:
            print("You chose " + fruit)
            