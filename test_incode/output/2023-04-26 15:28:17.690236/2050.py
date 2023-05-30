#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        print("Enter your choice:")
        choice = input("Choose your choice: ")
        if choice == "quit":
            break
        else:
            print("You chose:", choice)
