#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input and enumerates a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number == -1:
            break
        print('The number you entered is', number)
        
    
<|/ file source=github ext=.py |>