#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or calculates a list of numbers. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("You chose apple")
        elif fruit == "orange":
            print("You chose orange")
        elif fruit == "banana":
            print("You chose banana")
        else:
            print("You chose something else")
