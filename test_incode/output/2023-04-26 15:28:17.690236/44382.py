#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("Oh no! You entered an apple.")
        elif fruit == "banana":
            print("Oh no! You entered a banana.")
        elif fruit == "cherry":
            print("Oh no! You entered a cherry.")
        else:
            print("Oh no! You entered something else.")
