#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        choice = input("Do you want to quit? [y/N]")
        if choice == 'y':
            break
        elif choice == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")
