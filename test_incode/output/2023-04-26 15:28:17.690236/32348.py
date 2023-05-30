#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input or opens user input. """    
    while True:
        answer = input("Enter your answer: ")
        if answer == "quit":
            break
        elif answer == "quit\n":
            break
        elif answer == "exit\n":
            break
        else:
            print("You entered an invalid answer. Try again.")
