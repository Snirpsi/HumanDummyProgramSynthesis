#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input. """    
    while True:
        choice = input("Enter your choice: ")
        if choice == "quit":
            break
        else:
            print(choice)
