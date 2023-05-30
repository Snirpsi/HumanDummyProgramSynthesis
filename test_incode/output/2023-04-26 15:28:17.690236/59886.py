#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or enumerates fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "quit":
            break
        else:
            print("The fruit is", fruit)
            