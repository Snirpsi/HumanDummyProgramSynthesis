#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or opens user input. """    
    while True:
        answer = input("Do you want to continue? [y/n] ")
        if answer.lower() == "y":
            break
        else:
            print("Sorry, I didn't quite get that.")
    
<|/ file ext=.py source=github |>