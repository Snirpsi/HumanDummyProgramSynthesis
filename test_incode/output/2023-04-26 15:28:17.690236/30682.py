#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    # Remove all numbers from list
    numbers = [x for x in numbers if x not in [1,2,3,4,5,6,7,8,9,10]]
    
    # Print the result
    print(numbers)
    
    # Stop the loop
    break
    
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

<|/ file source=github ext=.py |>