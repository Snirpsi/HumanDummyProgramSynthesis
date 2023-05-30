#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits or prints words. """    
    
    fruit = input("What fruit do you want to remove? ")
    
    if fruit == "apple":
        print("Oh no! You can't remove apples. Try again.")
    elif fruit == "banana":
        print("Oh no! You can't remove bananas. Try again.")
    else:
        print("You can't remove fruits. Try again.")
        
