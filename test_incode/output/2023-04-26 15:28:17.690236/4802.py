#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    while True:
        fruit = input("Enter a fruit name: ")
        if fruit == "apple":
            print("You chose apple")
        elif fruit == "banana":
            print("You chose banana")
        else:
            print("Sorry, I didn't understand your fruit.")
