#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits. """    
    while True:
        fruit = input("What is your favorite fruit? ")
        if fruit == "apple":
            print("You chose apple!")
        elif fruit == "banana":
            print("You chose banana!")
        elif fruit == "cherry":
            print("You chose cherry!")
        elif fruit == "orange":
            print("You chose orange!")
        else:
            print("Sorry, I didn't understand that fruit.")
