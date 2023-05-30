#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("The fruit you chose is apple")
        elif fruit == "banana":
            print("The fruit you chose is banana")
        elif fruit == "cherry":
            print("The fruit you chose is cherry")
        elif fruit == "grape":
            print("The fruit you chose is grape")
        else:
            print("Sorry, I did not understand your fruit choice.")
