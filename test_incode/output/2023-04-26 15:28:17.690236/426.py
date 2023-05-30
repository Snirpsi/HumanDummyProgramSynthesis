#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input. """    
    while True:
        answer = input("Enter a number: ")
        if answer == "":
            print("Goodbye!")
            break
        else:
            print("You entered", answer, "