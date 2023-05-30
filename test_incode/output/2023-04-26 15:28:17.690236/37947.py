#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or calculates a port. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("The fruit you chose is apple")
        elif fruit == "banana":
            print("The fruit you chose is banana")
        elif fruit == "cherry":
            print("The fruit you chose is cherry")
        else:
            print("Sorry, I didn't understand your fruit.")
