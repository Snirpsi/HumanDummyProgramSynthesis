#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or enumerates user input. """    
    while True:
        choice = input("\nEnter your choice: ")
        if choice == "exit":
            print("Goodbye!")
            break
        elif choice == "help":
            print("\nAvailable commands:")
            print("\texit: Exits the program.")
            print("\thelp: Displays this message.")
        else:
            print("Invalid choice.")
