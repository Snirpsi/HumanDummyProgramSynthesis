#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or converts a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("Invalid input.")
        else:
            print("The number is", number)
            break
        
    
<|/ file source=github |>