#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "banana":
            print("You chose banana")
        else:
            print("You chose " + fruit)
