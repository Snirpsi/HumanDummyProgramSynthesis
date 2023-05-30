#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and opens user input. """    
    
    # Open the file that contains the user input
    file = open('input.txt', 'r')
    
    # Iterate over the user input and print it to the screen
    for line in file:
        print(line)
        
    # Close the file that contains the user input
    file.close()
<|/ file ext=.py source=github |>