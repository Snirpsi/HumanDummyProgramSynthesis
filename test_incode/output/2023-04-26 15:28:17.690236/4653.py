#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or iterates over a list of numbers. """    
    import sys
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
        
    
<|/ file source=github ext=.py |>