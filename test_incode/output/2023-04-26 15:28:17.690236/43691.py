#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or removes fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("You chose apple!")
        elif fruit == "orange":
            print("You chose orange!")
        elif fruit == "banana":
            print("You chose banana!")
        elif fruit == "cherry":
            print("You chose cherry!")
        elif fruit == "grape":
            print("You chose grape!")
        else:
            print("Sorry, I didn't understand your fruit.")
