#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or removes user input. """    
    while True:
        answer = input("Enter your choice: ")
        if answer == "exit":
            print("Goodbye!")
            break
        elif answer == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
