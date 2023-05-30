#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input. """    
    while True:
        answer = input("Do you want to quit? [y/n] ")
        if answer.lower() == "y":
            break
        else:
            print("Sorry, I didn't get that.")

<|/ file source=github ext=.py |>