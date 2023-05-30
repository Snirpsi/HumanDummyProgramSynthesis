#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        choice = input("\nEnter your choice: ")
        if choice == "quit":
            break
        elif choice == "quit2":
            break
        else:
            print(choice)
