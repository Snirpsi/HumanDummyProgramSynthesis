#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        answer = input("Enter your choice: ")
        if answer == "exit":
            break
        else:
            print("You chose " + answer)
