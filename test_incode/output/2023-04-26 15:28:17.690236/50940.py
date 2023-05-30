#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        choice = input("Enter your choice: ")
        if choice == 'exit':
            break
        else:
            print(choice)
