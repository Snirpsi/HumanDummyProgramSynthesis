#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of numbers and removes a list of words. """    
    
    # Read input from STDIN
    numbers = map(int, sys.stdin.readline().split())
    
    # Remove all words from numbers, leaving only numbers
    numbers = map(lambda x: x if isinstance(x, str) else int(x), numbers)
    
    # Print the result
    print(" ".join(map(str, numbers)))

<|/ file filename=remove_words.py |>