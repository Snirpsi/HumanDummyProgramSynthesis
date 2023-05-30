#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port or multiplyes a port. """    
    port = int(sys.argv[1])
    multiplier = int(sys.argv[2])
    
    if port > multiplier:
        multiplier = port
        
    print(multiplier * port)

<|/ file ext=.py |>