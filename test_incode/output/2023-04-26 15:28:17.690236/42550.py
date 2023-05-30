#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        answer = input("Do you really want to quit? [y/N] ")
        if answer.lower() == "y":
            break
        else:
            print("Sorry, I didn't quite get that. Try again.")
