#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or removes numbers. """    
    while True:
        fruits = input("Enter fruits: ")
        if fruits == "quit":
            break
        else:
            fruits = int(fruits)
            print(