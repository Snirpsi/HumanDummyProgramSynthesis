#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds fruits or removes a port. """    
    
    fruit = input("Please enter the fruit you want to add: ")
    
    if fruit == "apple":
        print("You added a fruit!")
    elif fruit == "orange":
        print("You removed a fruit!")
    else:
        print("That fruit does not exist!")
        
