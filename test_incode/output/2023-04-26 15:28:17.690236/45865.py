#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or prints user input. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Try again.")
            continue
    
    print("You entered ", number, " 