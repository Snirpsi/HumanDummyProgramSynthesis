#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input. """    
    while True:
        choice = input("Do you want to continue? [y/n]")
        if choice.lower() == 'y':
            break
        elif choice.lower() == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")
    
