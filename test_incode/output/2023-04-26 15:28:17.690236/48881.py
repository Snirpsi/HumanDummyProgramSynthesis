#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input or adds fruits. """    
    while True:
        fruit = input("What fruit do you want? ")
        if fruit == "apple":
            print("You chose apple")
        elif fruit == "orange":
            print("You chose orange")
        else:
            print("You chose a wrong fruit")
