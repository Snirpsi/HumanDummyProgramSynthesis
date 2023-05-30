#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        answer = input("Would you like to continue? [Y/n]")
        if answer == 'Y':
            break
        elif answer == 'n':
            break
        else:
            print("Invalid input.")
    
    
<|/ file ext=.py source=github |>