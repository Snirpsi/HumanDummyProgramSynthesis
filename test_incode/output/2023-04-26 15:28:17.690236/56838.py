#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers and stores a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    removeNumbers(filename)
    
    print("Done.")

<|/ file filename=removeNumbers.py ext=.py |>