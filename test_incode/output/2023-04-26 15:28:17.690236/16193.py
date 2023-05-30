#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        print("Enter your choice:")
        choice = input("(1-2): ")
        if choice == '1':
            print("You chose option 1")
        elif choice == '2':
            print("You chose option 2")
        else:
            print("Invalid choice.")
