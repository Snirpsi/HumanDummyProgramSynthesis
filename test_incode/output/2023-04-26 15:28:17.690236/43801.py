#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits or converts numbers. """    
    
    fruit = input("Enter a fruit name: ")
    
    if fruit == "apple":
        print("The fruit " + fruit + " was removed.")
    elif fruit == "banana":
        print("The fruit " + fruit + " was converted to a number.")
    else:
        print("The fruit " + fruit + " was not recognized.")
    
