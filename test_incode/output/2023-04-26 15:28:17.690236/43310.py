#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("You chose apple")
        elif fruit == "banana":
            print("You chose banana")
        elif fruit == "cherry":
            print("You chose cherry")
        else:
            print("You chose " + fruit)
