#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 portcalculator.py <port>")
        exit(1)
    
    port = sys.argv[1]
    
    print("Calculating port {}...".format(port))
    
    calculate(port)
    
    print("Done.")

<|/ file source=github ext=.py |>