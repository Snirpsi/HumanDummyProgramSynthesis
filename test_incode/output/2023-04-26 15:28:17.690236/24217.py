#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input. """    
    while True:
        answer = input("Enter a number: ")
        answer = int(answer)
        if answer > 100 or answer < 1:
            print("Sorry, that's not a number!")
        else:
            break
    
<|/ file source=github filename=