#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers. """    
    import sys
    numbers = [int(x) for x in sys.argv[1:]]
    for number in numbers:
        print(number)

<|/ file filename=