#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or opens a list of numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            if number > 0:
                print("You entered a positive number!")
            else:
                print("You entered a negative number!")
        except ValueError:
            print("Invalid input!")
        else:
            break
    
    
<|/ file source=github filename=