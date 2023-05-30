#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        print("Enter a number:")
        number = input("Enter a number: ")
        if number == "":
            print("You entered an empty string")
        else:
            print("You entered a number")
            break
        
    
<|/ file source=github filename=