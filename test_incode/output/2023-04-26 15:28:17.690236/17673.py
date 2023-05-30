#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input. """    
    while True:
        answer = input("Enter a number: ")
        answer = int(answer)
        if answer == -1:
            print("Invalid input. Try again.")
        else:
            print("You entered", answer, "