#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits or adds a port. """    
    while True:
        fruit = input("What is your favorite fruit? ")
        if fruit == "apple":
            print("Oh no! You chose apple!")
        elif fruit == "banana":
            print("Oh no! You chose banana!")
        elif fruit == "cherry":
            print("Oh no! You chose cherry!")
        elif fruit == "orange":
            print("Oh no! You chose orange!")
        else:
            print("Oh no! You chose something else!")
