#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or returns numbers. """    
    port = int(sys.argv[1])
    
    # Remove all numbers from list
    numbers = remove_numbers(sys.argv[2])
    
    # Return all numbers from list
    return numbers

<|/ file source=github ext=.py |>