#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input. """    
    while True:
        answer = input("Please enter your answer: ")
        if answer == "yes":
            print("Thanks for playing!")
            break
        elif answer == "no":
            print("Goodbye!")
            break
        else:
            print("Sorry, I didn't understand that.")
