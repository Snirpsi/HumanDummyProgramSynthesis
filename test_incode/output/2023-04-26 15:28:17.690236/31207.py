#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("The fruit you entered is apple!")
        elif fruit == "orange":
            print("The fruit you entered is orange!")
        elif fruit == "banana":
            print("The fruit you entered is banana!")
        else:
            print("Sorry, I didn't understand that.")
