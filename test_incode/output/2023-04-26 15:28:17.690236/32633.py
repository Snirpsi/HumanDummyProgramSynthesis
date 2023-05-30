#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    while True:
        fruits = input("How many fruits?")
        if fruits == "quit":
            break
        else:
            print("You chose:", fruits)
            
