#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or calculates a list of numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number == -1:
            break
        else:
            print(number)
    
    
<|/ file source=github |>