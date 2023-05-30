#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input. """    
    while True:
        choice = input("\nWhat would you like to do? ")
        if choice == "quit":
            break
        else:
            print(choice)
