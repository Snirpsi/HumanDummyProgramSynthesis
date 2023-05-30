#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    
    # Get the words from the command line
    words = sys.argv[1:]
    
    # Convert each word to a number
    numbers = [int(word) for word in words]
    
    # Print the numbers
    print('\n'.join(map(str, numbers)))

<|/ file source=github ext=.py |>