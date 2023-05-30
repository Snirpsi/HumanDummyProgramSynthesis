#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input. """    
    while True:
        print("Enter your choice: ")
        choice = input()
        if choice == "quit":
            break
        else:
            print(choice)
            
