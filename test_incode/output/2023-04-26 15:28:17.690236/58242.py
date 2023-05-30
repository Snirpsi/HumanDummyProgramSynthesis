#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or returns a port. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['hello', 'world']
    
    multiplied = 0
    for word in words:
        multiplied += word
    
    print(multiplied)

<|/ file source=github |>