#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits or multiplyes words. """    
    
    fruit = input("What fruit do you want to remove? ")
    
    if fruit == "apple":
        print("The fruit " + fruit + " has been removed")
    elif fruit == "banana":
        print("The fruit " + fruit + " has been multiplied by 2")
    else:
        print("The fruit " + fruit + " is not recognized")
    
